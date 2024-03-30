// given this is the input python code: 
// import numpy as np
// import scipy as sp
// def hello_world():
//     print("Hello world")

// then the request body would be: 
const inputs = '{start token}import numpy as np\nimport scipy as sp\n{end token}def hello_world():\n    print("Hello world"){middle token}'
const data = { inputs, ...configuration.requestBody };

const model = configuration.modelId;
let endpoint;
switch(configuration.backend) {
    case "huggingface":
        let url;
        if (configuration.url === null) {
          url = "https://api-inference.huggingface.co";
        } else {
          url = configuration.url;
        }
        endpoint = `${url}/models/${model}`;
        break;
    case "ollama":
    case "openai":
    case "tgi":
        endpoint = configuration.url;
        break;
}

const res = await fetch(endpoint, {
    body: JSON.stringify(data),
    headers,
    method: "POST"
});

// configure tokenizers
{
  "llm.tokenizer": {
    "repository": "myusername/myrepo",
    "api_token": null,
  }
}

const json = await res.json() as { generated_text: string };
