# DDos-detection-Using-Machine-Learning
## **What is DDOs(Distributed denial of service)?**
A Distributed Denial of Service (DDoS) attack is a malicious attempt to disrupt the regular functioning of a network, service, website, or online resource by overwhelming it with a flood of internet traffic. In a DDoS attack, multiple compromised computers or devices (often referred to as "botnets") are coordinated to send an excessive volume of data requests or traffic to the target, making it difficult or impossible for legitimate users to access the targeted resource. A ddos attack usually occurs in layer-7(Application-layer),layer-4(Transport-layer) and layer-3(Network-layer) of the Networking model. In this work we try to detect a DDos attack in the layer-7 using machine-learning algorithms(Random-forests and Gradient-Boosting).
## **What is a Botnet**
A botnet is a network of compromised computers or devices controlled by a single entity, often a cybercriminal or hacker, without the owners' knowledge. These compromised devices, referred to as "bots" or "zombies," can be infected with malware, allowing the attacker to commandeer them remotely.
In DDoS attacks, botnets are used to amplify and distribute attack traffic. The attacker instructs the bots to simultaneously send a flood of requests to the target, overwhelming its resources. Since botnets can consist of thousands or even millions of devices, they generate a massive volume of traffic, making it difficult for the target to distinguish legitimate requests from the malicious ones.
## **Different types of DDos attacks in layer-7**
### **Slowloris attack**
A Slowloris attack is a type of DDoS attack that targets web servers. It works by opening multiple connections to the server and sending partial HTTP requests, keeping them open by sending data very slowly. This ties up server resources, preventing new connections and legitimate requests. Slowloris doesn't require a large number of attacking machines, making it hard to detect. It focuses on resource exhaustion, causing the server to become slow or unresponsive.
### **HTTP GET/POST flood attack**
An HTTP GET/POST flood attack is a type of DDoS attack that targets web servers. Attackers send a massive number of GET or POST requests to overwhelm the server's capacity. GET requests retrieve data, while POST requests send data to the server, both tying up server resources. This flood of requests can slow down or crash the server, making the targeted website or application inaccessible. 
## **Dataset description**
The dataset has two sets balanced dataset and imbalanced dataset both with 84 features. The balanced dataset has 50% benign flows and 50% Ddos flows. The main goal of this work is to detect ddos attacks in application layers in which the  attack traffic is in smaller proportion when compared to benign flows hence imbalnced dataset is used which has 83% benign flows and 17% Ddos flows. The total number of benign flows in imbalnced dataset are 6321980 and total number of Ddos flows in the imbalanced dataset are 1294529.
## **<img width="291" alt="Screenshot 2023-10-09 215033" src="https://github.com/KolanHarsha/DDos-detection-Using-Machine-Learning/assets/110462466/1161405f-2586-4911-ab09-be2f82675f6b">**
## **Tools**
<img src="https://github.com/KolanHarsha/DDos-detection-Using-Machine-Learning/assets/110462466/88e29b73-06a2-48ac-8e80-0cd755dd980e" alt="jup" width="150" height="100">
<img src="https://github.com/KolanHarsha/DDos-detection-Using-Machine-Learning/assets/110462466/ec05c02a-389a-4363-8b8c-9b1ba8ca28b0" alt="python" width="150" height="100">
<img src="https://github.com/KolanHarsha/DDos-detection-Using-Machine-Learning/assets/110462466/91408e94-709a-4639-b3ce-72995848c519" alt="azure" width="175" height="100">

## **How to run the Notebook**
### **Quick start on a local machine**
1. Open a terminal in the project folder.
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Download the Kaggle dataset mentioned in `Dataset/Readme.md`.
4. Put `unbalaced_20_80_dataset.csv` in the project root, next to `Ddos.ipynb`.
5. Run the smoke test before opening the notebook:
```bash
python smoke_test.py
```
6. Launch Jupyter:
```bash
jupyter notebook
```
7. Open `Ddos.ipynb` and run the cells from top to bottom.

### **What the smoke test checks**
- Required Python packages are installed.
- The expected dataset CSV exists in the correct location.
- The CSV can be opened by pandas.
- Key columns used by the notebook are present.

### **Install Neccessary packages**
Ip-Address:
```bash
pip install ipaddress
 ```
Numpy:
```bash
pip install numpy
 ```
Pandas:
```bash
pip install pandas
 ```
Matplotlib:
```bash
pip install matplotlib
 ```
Seaborn:
```bash
pip install seaborn
 ```
Scikit-learn:
```bash
pip install scikit-learn
 ```
### **Running on Azure Cloud Platform**
1. Go to the [Azure Machine Learning ](https://azure.microsoft.com/en-us/products/machine-learning) platform and launch Azure Machine learning studio.
2. Once the studio is launched go to the compute section and choose a compute instance. The compute instace which I choosed has the following specifications Standard_E8s_v3 
   (8 cores, 64 GB RAM, 128 GB disk).
3. After the compute instance is created launch the jupyter notebook which can be found again in the compute section.
4. Install the packages which I mentioned above and run the "Ddos.pynb" file.
## **Methodology**
**Random-Forests**:
1. A Random Forest is an ensemble model that builds upon the concepts of bagging and decision trees.
2. It creates multiple decision trees, usually using a random subset of features for each tree.
3. For each tree, it uses bootstrapped samples from the training data.
4. During prediction, the Random Forest combines the outputs of all the trees, typically using majority voting for classification and averaging for regression.
5. The key to the success of Random Forest is the diversity and randomness introduced by using both bootstrapped samples and random subsets of features for each tree.

**Hyper-parameter Tuning**:

1. The model is trained using hyper-parameter tuning  by implementing grid-search with 3-fold cross validation to prevent over-fitting.

<img width="735" alt="Screenshot 2023-10-25 145406" src="https://github.com/KolanHarsha/DDos-detection-Using-Machine-Learning/assets/110462466/d25425ad-60fb-4c51-92ea-1782e2760814">

2. Once the grid-search is done best parameters are evaluated and the model is trained again using the best parameters.

<img width="735" alt="image" src="https://github.com/KolanHarsha/DDos-detection-Using-Machine-Learning/assets/110462466/657154fe-d499-4342-aab1-91fd18191348">

## **Evaluating the performance of the Model**
**Accuracy**:
The model has an impressive accuracy of 99.9% on validation data with only 4 mis-classifications.
<img width="735" alt="Screenshot 2023-10-25 142608" src="https://github.com/KolanHarsha/DDos-detection-Using-Machine-Learning/assets/110462466/b89581d0-a0bf-4f5a-b0cb-86e451b4abae">

**Confusion-Matrix**:

<img width="435" alt="Screenshot 2023-10-09 215053" src="https://github.com/KolanHarsha/DDos-detection-Using-Machine-Learning/assets/110462466/e0478576-1b1f-4fca-bd6d-cc2c3bd79cc2">

1. True Positives (TP): 427,005 (DDoS cases correctly predicted as DDoS)
2. True Negatives (TN): 2,070,680 (Normal cases correctly predicted as Normal)
3. False Positives (FP): 0 (Normal cases incorrectly predicted as DDoS)
4. False Negatives (FN): 4 (DDoS cases incorrectly predicted as Normal)
5. Precision: Precision is the ratio of correctly predicted DDoS cases to all cases predicted as DDoS.

     Precision = TP / (TP + FP) = 427,005 / (427,005 + 0) = 1.0

     The precision is 1.0, indicating that when the model predicts an instance as DDoS, it is always correct.

7. Recall (Sensitivity): Recall is the ratio of correctly predicted DDoS cases to all actual DDoS cases.

     Recall = TP / (TP + FN) = 427,005 / (427,005 + 4) ≈ 0.9999

     The recall is very close to 1.0, indicating that the model effectively identifies nearly all of the actual DDoS cases.
9. F1-Score: The F1-score is the harmonic mean of precision and recall and provides a balance between the two metrics.

     F1-Score = 2 * (Precision * Recall) / (Precision + Recall)

     F1-Score = 2 * (1.0 * 0.9999) / (1.0 + 0.9999) ≈ 0.9999

     The F1-score is very close to 1.0, indicating that the model achieves a high balance between precision and recall.

Based on the precision, recall, and F1-score, the model appears to perform exceptionally well for DDoS detection. It has high precision, meaning that when it predicts an instance as DDoS, it is almost always correct, and it has high recall, indicating that it effectively captures nearly all the actual DDoS cases.

**ROC-Curve**:
AUC(Area under ROC-Curve) measures the performance of a binary classification model, the Area under ROC-Curve is close to 1.0 which indicates the model almost classifies perfectly.

<img width="435" alt="Screenshot 2023-10-09 215113" src="https://github.com/KolanHarsha/DDos-detection-Using-Machine-Learning/assets/110462466/97cac5df-89b7-4514-9e74-9a278de8b764">

## **Top-10 Features**
<img width="578" alt="Screenshot 2023-10-09 215134" src="https://github.com/KolanHarsha/DDos-detection-Using-Machine-Learning/assets/110462466/31ba3546-5881-4992-b2cf-69c64baa9986">

1. Importance provides a score of the feature. Higher the score, major the role in making a decision in building a tree. The top 10 important features returned by trained 
RF-model are shown in above figure.

2. "Src Ip","Dst Ip","Src Port","Dst Port", are in the top 10 features which makes sense as these four are combined to determine the "Flow ID" which describes the entire flow.

## **Contributors**
- Sai Harsha Vardhan Reddy, Kolan- skolan@horizon.csueastbay.edu, harsha62334@gmail.com

Thanks for reading!
