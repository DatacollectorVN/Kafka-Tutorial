# Kafka-Tutorial

## Prerequirements
- Install Java or JDK. If not, follow our instrunction [here](https://github.com/DatacollectorVN/PySpark-Tutorial/tree/master/setup-PySpark). Verification:
```bash
java --version
```

## Setup for Mac M1
- Install kafka:
```bash
brew install kafka
```

- Add to root PATH:
```
nano ~/.zshrc
```
The add new line `export PATH="/opt/homebrew/Cellar/kafka/3.2.0/bin/:$PATH"`.

- Check Kafka version
```bash
kafka-topics --version
```