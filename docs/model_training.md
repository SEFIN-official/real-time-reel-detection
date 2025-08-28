# Model Training and Evaluation

## Model Architecture
We used a Random Forest Classifier with the following parameters:
- `n_estimators`: 100
- `random_state`: 42

Features used for training:
- packet_size
- duration
- protocol_code
- network_code

## Training Procedure
- Dataset was split into 75% training and 25% test using stratification on labels.
- Model training was performed on training data only.

## Evaluation
- Test set accuracy and F1 score were near perfect (accuracy ~ 100%).
- 5-fold cross-validation yielded a mean macro F1 score of approximately 0.985.
- Confusion matrix showed minimal misclassifications.

## Feature Importance
- Duration was the most influential feature followed by packet size and protocol.
