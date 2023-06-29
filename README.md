# leaf_disease_pred
This is website in which you can upload leaf to find weather your plant has disease 





Abstract:
This project aims to develop an image classification system to identify leaf
diseases. The system employs various feature extraction techniques,
including Local Binary Patterns (LBP), Gray-Level Co-occurrence Matrix
(GLCM), and Histogram of Oriented Gradients (HoG), combined with
different classification algorithms such as Support Vector Machines (SVM)
and K-Nearest Neighbors (KNN). The performance of each combination is
evaluated using accuracy as the primary metric.
1. Introduction:
Leaf disease identification plays a crucial role in agriculture for early
detection and prevention of plant diseases. Automated image classification
techniques provide a non-destructive and efficient solution for detecting leaf
diseases. In this project, we explore different feature extraction techniques
and classification algorithms to accurately classify leaf disease images.
2. Project Aim:
The aim of this project is to develop an image classification system that can
accurately identify leaf diseases. The system utilizes various feature
extraction techniques, including LBP, GLCM, and HoG, in combination with
SVM and KNN classifiers. The performance of each combination is
evaluated, and the highest accuracy combination is determined.
3. Methodology:
Dataset: The dataset consists of labeled leaf disease images, including
multiple classes representing different diseases.
Feature Extraction:
Local Binary Patterns (LBP): Captures local texture information by
encoding the relationship between a pixel and its neighbors.
Gray-Level Co-occurrence Matrix (GLCM): Extracts texture features
based on the spatial distribution of gray-level values.
Histogram of Oriented Gradients (HoG): Computes the gradient
magnitude and orientation to represent image features.
Classification Algorithms:
Support Vector Machines (SVM): A supervised learning algorithm that
separates data using hyperplanes.
K-Nearest Neighbors (KNN): A non-parametric algorithm that classifies
data based on the majority class of its k nearest neighbors.
Here is the step involved in this project:
❖ Leaf Image Dataset: The dataset consists of labeled leaf disease
images used for training and evaluation.
❖ Preprocessing: This block involves any necessary preprocessing
steps such as resizing, normalization, and noise removal to
enhance the quality and consistency of the input images.
❖ Feature Extraction: Various feature extraction techniques (LBP,
GLCM, HoG) are applied to extract relevant information from the
preprocessed images. Each technique generates a set of
features that capture different aspects of the leaf images.
❖ Classification: The extracted features are used as input to
different classification algorithms (SVM, KNN). These algorithms
learn patterns and relationships in the feature space to classify
the leaf images into different disease classes.
❖ Evaluation: The performance of each classification algorithm and
feature extraction technique combination is evaluated using
metrics such as accuracy, precision, recall, and F1-score. This
step helps determine the effectiveness of each combination in
accurately classifying leaf diseases.
❖ Results: The results, including accuracy scores for each
combination, are presented to compare the performance of
different techniques and algorithms.
4. Results and Analysis:
The accuracy results for each combination of feature extraction techniques
and classification algorithms are as follows:
LBP with SVM: Accuracy - 0.76
LBP with KNN: Accuracy - 0.72
GLCM with SVM: Accuracy - 0.66
GLCM with KNN: Accuracy - 0.67
HoG with SVM: Accuracy - 0.74
HoG with KNN: Accuracy - 0.86
Fig1.1:confusion matrix
From the results, it can be observed that the combination of HoG feature
extraction with SVM classification achieved the highest accuracy of 0.88,
indicating superior performance in leaf disease classification.
Table1.2:classification_report
Let's analyze the results in more detail:
1. LBP with SVM (Accuracy - 0.76):
● The combination of Local Binary Patterns (LBP) for feature extraction
and Support Vector Machines (SVM) for classification achieved an
accuracy of 0.76.
● LBP captures local texture information, and SVM is a powerful
classifier for separating data.
● This combination performed moderately well, but there is room for
improvement.
2.GLCM with SVM (Accuracy - 0.66):
● The combination of Gray-Level Co-occurrence Matrix (GLCM) for
feature extraction and SVM for classification achieved an accuracy of
0.66.
● GLCM extracts texture features based on the spatial distribution of
gray-level values.
● Although SVM is a powerful classifier, the accuracy obtained in this
combination is relatively lower compared to others.
3.GLCM with KNN (Accuracy - 0.67):
● The combination of GLCM for feature extraction and KNN for
classification achieved an accuracy of 0.67.
● Despite KNN's simplicity, it also yielded a lower accuracy in
combination with GLCM.
4.HoG with SVM (Accuracy - 0.74):
● The combination of Histogram of Oriented Gradients (HoG) for
feature extraction and SVM for classification achieved an accuracy of
0.74.
   ![image](https://github.com/krishnakumarbhat/leaf_disease_pred/assets/79183768/2a875943-2481-4771-8ff9-0c095c2dc6af)

● HoG captures gradient information and has been successful in
various image classification tasks.
● SVM provided better accuracy compared to other classification
algorithms in combination with HoG.
5.HoG with KNN (Accuracy - 0.86):
● The combination of HoG for feature extraction and KNN for
classification achieved the highest accuracy of 0.86.
● This combination performed exceptionally well, outperforming all
other combinations.
● KNN, when combined with HoG, was able to capture relevant image
features and classify them accurately.
![image](https://github.com/krishnakumarbhat/leaf_disease_pred/assets/79183768/e40552f7-87b8-48b1-9de2-308e35d063b9)

Overall Analysis:
● Among the feature extraction techniques, HoG demonstrated the best
performance, achieving the highest accuracy in combination with both
SVM and KNN.
● KNN performed relatively better when combined with HoG compared
to other feature extraction techniques.
● GLCM showed lower accuracy in both SVM and KNN combinations.
● SVM generally performed well with HoG and LBP features, while
KNN had better performance with HoG.
5. Conclusion:
In this project, we developed an image classification system to identify leaf
diseases using different feature extraction techniques and classification
algorithms. The combination of HoG feature extraction with SVM
classification achieved the highest accuracy of 0.88, outperforming other
combinations. The results demonstrate the effectiveness of combining HoG
features with SVM for accurate leaf disease classification. However, further
investigations and optimizations can be performed to enhance the system's
performance and explore other feature extraction and classification
techniques
