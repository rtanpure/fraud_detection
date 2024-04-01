# Dataset Description

## Overview

This dataset contains information about fraudulent transactions collected over a period of six months. The data includes various features such as transaction type, transaction amount, old balance before the transaction, new balance after the transaction, and whether the transaction was flagged as fraudulent or not.

## Content

The dataset consists of the following columns:

1. `TransactionID`: Unique identifier for each transaction.
2. `TransactionType`: Type of transaction (e.g., 1 for transfer, 2 for payment).
3. `Amount`: Amount of the transaction.
4. `OldBalanceOrig`: Old balance before the transaction for the originating account.
5. `NewBalanceOrig`: New balance after the transaction for the originating account.
6. `OldBalanceDest`: Old balance before the transaction for the destination account.
7. `NewBalanceDest`: New balance after the transaction for the destination account.
8. `IsFraud`: Binary indicator (0 or 1) representing whether the transaction is fraudulent.
9. `IsFlaggedFraud`: Binary indicator (0 or 1) representing whether the transaction was flagged as fraudulent by the system.

## Acknowledgements

The dataset is sourced from [XYZ Bank](https://www.xyzbank.com) and was collected for research purposes.

