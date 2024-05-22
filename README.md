# Fine-tuning Llama2-7B-Chat for Privacy Policy Q&A and Summarization
__By Chris Puzzo and Christain Jackson__

__For Comp741/841__

__README updated: 5/22/24__

The basis of this problem is to fine-tune Meta's Llama 2 Transformer using PEFT
and QloRA in order to be able to analyze privacy Policies.

Privacy Policies are written to be confusing and extremely technical, so a tool
that helps users answer questions and summerize privacy policies can be very
useful in knowing how personal data is being used. the HOWTO.md file contains
simple instructions on running the tool

## Setup
This tool is designed to be used on colab with the huggingface transformers
library. The model (Llama-2-7b-privacy) is hosted on my (Chris Puzzo) 
personal [huggingface profile](https://huggingface.co/ChrisPuzzo) and is publically avalible. The model was trained
using a training code for llama from [Maxime Labonne](https://twitter.com/maximelabonne)
avalible [here](https://colab.research.google.com/drive/1PEQyJO1-f6j0S_XJ8DV50NkpzasXkrzd?usp=sharing)

There is no requirments file in this repo because it uses dependencies pre-installed
on colab.

## Results
We did some small amouts of testing on the model however we got pretty unconclusive data. As you can see in the rouge 
excel sheet, the scores weren't great. However we believe that the rouge testinging metric might not be the best way
to judge this.
