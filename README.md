# Keras: GitHub and StackOverflow Issues Analysis

-------------------------------

### Issues Analysis
This is a bucketization of issues into high-level categories. Ideally, these broad themes would be used to improve documentation and error messages for the API itself.

#### Documentation Enhancements

* How do I create custom loss or activation functions, or constraints?
* How can I ensure my model is reproducible?
* How do I use multiple tensor inputs (especially multiple tensor inputs with differing dimensions)?
* How can I do transfer learning (use pre-trained models) with Keras?
* How can I save some of my Keras layers to use in a new model?
* How can I visualize my Keras models in TensorBoard?

#### Error Message Enhancements

* I am experiencing an issue when working with multiple CPUs / GPUs.
* I am experiencing issues with non-TensorFlow backend (CNTK, Theano).
* I need clarification on how to build and configure an LSTM model.
* Troubleshooting for issues with loss and accuracy.
* Troubleshooting errors for input and output dimensions.
* Troubleshooting installation and virtual environment issues.

### Installation Woes
Deep dive into common installation issues - based on language (Python, R), operating system (Windows, Linux, Mac), corresponding deep learning framework (Theano, Cognitive Toolkit, TensorFlow), or development environment (RStudio, Anaconda).

### Usability Enhancements 
Several ideas for improving usability for TensorFlow and Keras.

* Release notes for humans.
* Dissection of methods and classes.
* More informative error messages.
* Scratch for Neural Networks

### Keyword Extraction from GitHub Issues
* `keyword_extractor.py`: script for extracting keywords from dumped GitHub issues
* `RAKE_output.csv`: keywords for body content
* `title_ouput.csv`: keywords for titles
* `keras_issues.csv`: full export of issues (June 2018)
