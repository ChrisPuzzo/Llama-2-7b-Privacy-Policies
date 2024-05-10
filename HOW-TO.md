# How To
## Steps in running the code
The model is trained using the privacyFineTune.ipynb file and is queried with
the privacyTest.ipynb file. There is no need to run the fine-tuning again as 
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