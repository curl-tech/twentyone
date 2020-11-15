![logo](/imgs/21_logo.png)

# TwentyOne (21)*
*Note 21 is still in alpha, there will be many changes in the next few months

## Introduction
We all know ["42"](https://en.wikipedia.org/wiki/Phrases_from_The_Hitchhiker%27s_Guide_to_the_Galaxy#Answer_to_the_Ultimate_Question_of_Life,_the_Universe,_and_Everything_(42)) is the answer to the ultimate question in the universe. 42 is the dream solution we all want to achieve. Today we are halfway there. TwentyOne is the engine which takes data and creates models and answers questions to many different kinds of problems. 21 is a generic tool which can be used in multiple use cases.

## Why use 21?

Solution = AI Expertise + Data -> 42 + Data ~ 21 + Data

Focus of 21 is to get an effective model quickly and reliably and it doesn't try to get state of the art model (though we can get best in class results). It is meant for non-data scientists to build models for their use cases. 

21 is designed to leverage transfer learning as much as possible. For many problems the data requirement for 21 is minimal. This saves a lot of time, effort and cost in data collection. Model training is also greatly reduced.

It can also be used in situations where data is private and can't be shared for training. We can use [Torpedo Blocks (TBs)]() to trigger 21 to start the ML training remotely. The trained model can be made available for inference using right set of TBs. This helps in using the intelligence and results derived from private data and maintaining the privacy at the same time.

Though 21 tries to be an auto ML engine, it can be used as an augmented ML engine which can help data scientist to quickly develop models. This can bring best of both worlds leading to "Real Intelligence = Artificial Intelligence + Human Intelligence"

### Advantages
- Greatly improves development time (days instead of months)
- Needs less amount of data (transfer learning and data augmentation)
- Cost for development is minimal (mainly compute cost, rest is reduced)
- Builds robust models (effectively searches "more space" to get best model)
- Learns best practices and uses them for similar use cases (leverages task-pipeline relation)
- Data Security and Privacy (remote training and inference using TBs)
- Works on most of the common use cases (contiguously adding new use cases)

### Drawbacks
- Needs a lot of compute
- Can't be used for new kind of problems or very complex problems

![meme](/imgs/memes/21_0.jpeg)

## How to use?

The configuration is through config.yaml file. Look at the test folder to see how to use 21.

## How does it work?

Read the docs to understand how it works. The architecture in the docs provide top level view of how things work. API documentation gives details of how to use 21 engine.

## Additional Resources

- [Architecture](docs/21_architecture.drawio)
- [Config](config/config.yaml)
- [Todos](docs/todo_logs.md)
- [References](docs/references.md)

## Maintained By

This repo is currently maintained by [shivaramkrs](https://github.com/shivaramkrs) and the ML team at [Curl Tech](www.curl.tech). We welcome your contribution.

## License

MIT License