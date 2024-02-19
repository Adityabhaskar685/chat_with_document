# Chat with PDF Locally

This project allows you to interact with your PDF documents in a conversational manner, all within a local setup employing open-source tools. This guide will walk you through the setup process.

## Installation Guide

### Prerequisites

Ensure you have Python installed on your system. This project has been tested on Python 3.7 and above.

### Install Dependencies

First, you'll need to install the required Python packages. Navigate to the project's root directory and run:

```sh
pip install -r requirement.txt
```

### Setting up the Ollama Server

#### 1. Download Ollama and Run 

For Linux users, you can download and install the Ollama server by executing:

```sh
curl -fsSL https://ollama.com/install.sh | sh
```

Run the ollama server

```sh
ollama serve
```


#### 2. Acquire the Model from Ollama Hub

Next, you'll need to pull the Zephyr model from the Ollama Hub. There are two approaches:

**Direct Run:**

Simply pull and run the Zephyr model using the command:

```sh
ollama run zephyr
```

**Local Download:**

Alternatively, to download and use the model locally:

- Download the model file with `wget`:

```sh
wget https://huggingface.co/TheBloke/zephyr-7B-beta-GGUF/resolve/main/zephyr-7b-beta.Q5_K_M.gguf?download=true
```

- Rename the downloaded model file for easier access:

```sh
mv zephyr-7b-beta.Q5_K_M.gguf?download=true zephyr-7b-beta.Q5_K_M.gguf
```

- Create the model in your Ollama setup:

```sh
ollama create zephyr -f modelFile
```

Replace `modelFile` with the path to the `zephyr-7b-beta.Q5_K_M.gguf` file.

### Running the Streamlit App

Finally, to interact with your PDF documents through the UI:

```sh
streamlit run app.py
```

This will start the Streamlit server, and you should be able to access the web application by navigating to the address shown in your terminal.

## Usage

Once the app is running, follow the on-screen instructions to upload your PDF documents and start chatting with them.

Happy chatting with your documents!