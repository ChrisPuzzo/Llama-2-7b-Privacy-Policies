# How To
## Steps in running the code
The model is trained using the privacyFineTune.ipynb file and is queried with
the testPrivacy.ipynb file. There is no need to run the fine-tuning again as 
the model is already avalible on huggingface however we will still give
instruction on how to do it.

## fine-tuning
Fine tuning is pretty simple as the majority of it has alread been set up for
easy use. If you wish to train the model the same as we did, just run
everything as is and then log in using your personal huggingface token.

If you wish to use a different model or dataset, then do the following 

* As this file is made specifically for fine-tuning Llama 2, we suggest keeping
the model_name variable untouced. However if you want to change it, change it to the 
model name you wish avalible in the Transformers Library.
* Change the dataset name to whatever dataset is desired (must be supported by 
huggingface dataset library).
* Change the new_model name to whatever you want.
* adjust the dataset_text_field="" variable to the name of the row of text in
your dataset. For example in the sjsq dataset the text column is called "Text".
* Change the prompt variable to a question you want to ask it.

Aside from these changes, run the file from top to bottom to train the model.
Should take about 25 minutes in total.

## Prompting
The testPrivacy.ipynb file contains the test prompts that were used to test the
model. It should be set to run as is with our model. If you wish to add custom
prompts to the file, do so by creating a new codeblock and using the syntax
```
prompt = "Your question"
```
We also provided two different privacy policies for refrence. The first is 
from [TopHive](https://tophive.ai/privacy-policy) and the second is from 
[Starbucks](https://www.starbucks.com/terms/privacy-policy/). The starbucks one
does not work as it is too big and you run out of GPU ram fast on the free
colab plus Llama doesn't like how many words are in it. 
TopHive does work however. To use these privacy policies in your prompt change
the policy variable to the name of the company you are using the policy of
```
policy = starbucks
```

Then run one of the question boxes or make your own prompt.

To run the text generation chose a prompt first by running that box then run
```
result = pipe(f"<s>[INST] {prompt} [/INST]")
print('\n',result[0]['generated_text'])
resultList.append(result[0]['generated_text'])
```
Other than that basically run the code from start to bottom until you get to
the prompt section. All prompts are saved in the "resultList" variable.