### Fine-Tuning Large Language Models (PROPOSAL.MD)

UNH - COMP741/841

Chris Puzzo, Christian Jackson

4/4/2024

#### I. Type of AI System Being Developed

We propose to fine-tune a Large Language Model (LLM) which is a type of deep learning model. These models are useful for natural language processing and text prediction and may be trained with a large amount of general purpose knowledge from Internet sources. However, in many cases, these models are not trained well enough to answer questions or draw on knowledge from specific domains. To address this gap, the process of Fine Tuning is used to augment or incorporate specific domain knowledge into the LLM.

It's useful to fine-tune an existing LLM versus simply retraining a model from the ground up because training an LLM is costly and time consuming. It can cost millions to hundreds of millions of dollars to train a large transformer model. The fine-tuning approach leverages the sunk cost and time of an existing general purpose LLM, but provides the benefit of narrow domain expertise for a specialty purpose.

#### II. AI System Selection

We are proposing the selection of the Llama 2 as our general LLM to fine-tune. We have three model sizes that we can experiment with from 7B to 70B parameters. In addition to Llama 2 we will be using the python PEFT library as our fine-tuning engine.

#### III. Content Knowledge Background

There are a couple of Content Knowledge areas that a good understanding of is essential to understanding how our project will function. The first AI paradigm that needs to be understood is Neural AI, particularly deep learning. This is very important due to how we will be fine tuning the model using PEFT instead of "standard'' fine tuning. PEFT differs in that instead of tuning all the parameters of a model, it only tunes "a small number of (extra) model parameters instead of all the model's parameters' '. Basically it can tune a model using a much smaller set of data to get results that, while not perfect, are good enough for the majority of use cases out there. This is also a reason that a basic knowledge of how fine-tuning works is important to this project. The ability to compare results of PEFT with that of standard fine-tuning will be important to the creation of our chatbot because it will show us if PEFT really is good enough or if full fine-tuning is required.

Also an understanding of what Transformers and Natural Language Processing (NLP) is important to our project as the model we are using Llama is a Transformer that is used for NLP.

#### IV. Practical Knowledge Background

The general steps required for LLM fine-tuning are:

1. Select a base pre-trained general purpose LLM
2. Select a dataset for a particular problem that is labeled so it can be used for training the model
3. Preprocess the dataset (data cleaning, split into training, validation, and test sets)
4. Fine-tuning to adapt the general LLM to our task using our training dataset.

Usually, this last fine-tuning step is done by updating the model's parameters based on the new training dataset. However, we've learned of new methods called parameter efficient fine-tuning (PEFT) and Low Rank Adaptation (LoRA) that avoid loading the entire LLM into memory and modifying its weights. Instead, we'll create additional smaller neural matrices called adapters that are used in combination with the original LLM for generating inferences.

Specifically, we'll use Quantized LoRA (QLoRA), which is a memory efficient way of creating an adapter for an existing LLM, but apparently still provides performance similar to the LoRA method. The original model's weights are left unchanged, and we have an adaptor that modifies the inferences of the LLM at runtime. An interesting additional benefit of this approach is that the LLM can be tuned for multiple purposes, and the resulting adapters can be swapped in and out or used currently against a single in-memory LLM.

The following steps have been adapted from an online tutorial1:

1. _Using Colab?_
2. _Install required libraries_
3. _Load dataset_
4. _Create Bitsandbytes configuration_
5. _Load the pre-trained model (Llama 2?)_
6. _Tokenization_
7. _Test the model with zero shot inferencing_
8. _Pre-process our dataset (TBD?)_
9. _Prepare the model for QLoRA_
10. _Setup PEFT for fine-tuning_
11. _Train the PEFT adapter_
12. _Evaluate the model qualitatively (human)_
13. _Evaluate the model quantitatively (ROUGE metric?)_

The LLM we're using is available from Meta in various parameter sizes at:
[https://llama.meta.com/llama2/](https://llama.meta.com/llama2/)

We expect that we may need to use the following libraries:

- **Bitsandbytes** to load the model efficiently
- **peft:** for efficient fine-tuning.
- **datasets:** a Hugging Face library for accessing datasets
- **einops:** for tensor operations.

#### V. Risks

**Algorithmic discrimination**
 The base LLM that we've selected (Llama2) most likely contains biases regardless of how careful the creators, Meta Corporation, have been to try to mitigate them. Also, we're introducing another dataset when fine-tuning and there is the potential for introducing new biases or amplifying existing biases in the model. These biases could be further propagated or even magnified in the fine-tuned model, leading to bad output (discriminatory, or inappropriate).

In order to avoid this our best bet would be to source our data from multiple different sources and carefully look it over before using it. This way we can at least avoid adding any bias to the system.

**Overfitting/Underfitting**
 Fine-tuning our LLM might lead to overfitting, especially if the dataset used for fine-tuning is not diverse enough or is too small. We will need to test to ensure this doesn't happen. We also want to avoid underfitting, because we are not working with a massive dataset we might need to supplement the chat data with other sources that are similar but not exactly the same.

**Protection of data privacy**
 We aren't planning to use datasets that contain PII. However, if our training dataset does happen to contain PII, we risk training our model in a way that could perpetuate a data breach or result in an unintended disclosure of confidential information.

In addition, where we source our data from can be a problem. The idea is to build a chatbot that is fine-tuned to talk like a specific person/group of people. However if we source our data from people who don't want their data shared that would be an invasion of their right of privacy.

**Misalignment**
 It's possible that our fine-tune model might not align perfectly with our expectations. If our approach of using QuLora does not adequately capture the nuances of the domain knowledge, we may not get the output that we're expecting.

**Compute resources**
 Our approach is to avoid resource intensive processing (within reason). Fine-tuning LLMs can be very expensive. Our hope is that by using Parameter Efficient Fine-Tuning (PEFT) versus Full Fine Tuning (Instruction fine-tuning), we can address this concern.

**Dependence on Proprietary Technologies**
 The LLM that we've selected to use (Llama 2) is open source and was pretrained on publicly sourced data. It's available in three sizes that range from 7B to 70B parameters that may help give us some interesting options for comparisons. This is a well known LLM provided by Meta with many open source libraries that will allow us to avoid a dependence on an expensive and rapidly changing technology like ChatGPT or Anthropic's Claude.

**Transparency and explanation**

Our AI model is a deep learning neural model and as such it operates much like a "black box." It will not be possible for us to provide an explanation for how any specific output was generated beyond pointing at the original LLM and the training data we've used for fine-tuning it. This is a general problem with this type of architecture and there is a lot of research happening right now to provide more explanation about how answers are developed. This is not something that we can address in this project.

####


#### VI. References

Amur, Dilli Prasad. 2023. "QLoRA: Fine-Tuning Large Language Models (LLM's)." _Medium_ (blog). November 28, 2023.[https://medium.com/@dillipprasad60/qlora-explained-a-deep-dive-into-parametric-efficient-fine-tuning-in-large-language-models-llms-c1a4794b1766](https://medium.com/@dillipprasad60/qlora-explained-a-deep-dive-into-parametric-efficient-fine-tuning-in-large-language-models-llms-c1a4794b1766).

Das, Suman. 2024. "Fine Tune Large Language Model (LLM) on a Custom Dataset with QLoRA." _Medium_ (blog). January 25, 2024.[https://dassum.medium.com/fine-tune-large-language-model-llm-on-a-custom-dataset-with-qlora-fb60abdeba07](https://dassum.medium.com/fine-tune-large-language-model-llm-on-a-custom-dataset-with-qlora-fb60abdeba07).

Dettmers, Tim, Artidoro Pagnoni, Ari Holtzman, and Luke Zettlemoyer. 2023. "QLoRA: Efficient Finetuning of Quantized LLMs." arXiv.[http://arxiv.org/abs/2305.14314](http://arxiv.org/abs/2305.14314).

"Governments Setting Limits on AI – Communications of the ACM." 2024. March 15, 2024.[https://cacm.acm.org/news/governments-setting-limits-on-ai/](https://cacm.acm.org/news/governments-setting-limits-on-ai/).

"PEFT." n.d. Accessed April 4, 2024.[https://huggingface.co/docs/peft/en/index](https://huggingface.co/docs/peft/en/index).

_1_[_https://dassum.medium.com/fine-tune-large-language-model-llm-on-a-custom-dataset-with-qlora-fb60abdeba07_](https://dassum.medium.com/fine-tune-large-language-model-llm-on-a-custom-dataset-with-qlora-fb60abdeba07)


**Tools and Libraries**

QLoRA - [https://github.com/artidoro/qlora](https://github.com/artidoro/qlora)

Bitsandbytes [https://github.com/TimDettmers/bitsandbytes](https://github.com/TimDettmers/bitsandbytes)

PEFT – [https://huggingface.co/docs/peft/en/package\_reference/config](https://huggingface.co/docs/peft/en/package_reference/config)

Datasets –

einops –: [https://github.com/arogozhnikov/einops](https://github.com/arogozhnikov/einops)
