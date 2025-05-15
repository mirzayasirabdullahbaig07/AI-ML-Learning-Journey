# Unsupervised Learning

## What is Unsupervised Learning?

Unsupervised learning is a type of machine learning where the model learns patterns from **unlabeled data**. There are no predefined labels or outputs. The goal is to discover hidden structures, groupings, or patterns in the data.

Unlike supervised learning, there’s no “correct answer” provided — the model explores the data and tries to organize it in meaningful ways.

---

## Types of Unsupervised Learning Tasks

1. **Clustering** – Group data into clusters based on similarity.
   - Example: Customer segmentation based on purchasing behavior.
2. **Dimensionality Reduction** – Reduce the number of features while preserving data structure.
   - Example: Visualizing high-dimensional data in 2D.

---

## Important Unsupervised Learning Algorithms

### 1. K-Means Clustering
- **Type**: Clustering
- **Use Case**: Grouping similar items.
- **Idea**: Divides data into ‘k’ clusters by minimizing the distance from the center of each cluster.

### 2. Hierarchical Clustering
- **Type**: Clustering
- **Use Case**: Creating dendrograms or tree-like cluster structures.
- **Idea**: Builds nested clusters by merging or splitting them successively.

### 3. DBSCAN (Density-Based Spatial Clustering)
- **Type**: Clustering
- **Use Case**: Clustering data with noise and irregular shapes.
- **Idea**: Groups together points that are closely packed and separates outliers.

### 4. Principal Component Analysis (PCA)
- **Type**: Dimensionality Reduction
- **Use Case**: Reducing complexity of data for visualization or modeling.
- **Idea**: Transforms data into a smaller number of uncorrelated components.

### 5. t-SNE (t-distributed Stochastic Neighbor Embedding)
- **Type**: Dimensionality Reduction / Visualization
- **Use Case**: Visualizing high-dimensional data in 2D or 3D.
- **Idea**: Preserves local relationships in data to visualize similar points close together.

### 6. Autoencoders (Neural Network Based)
- **Type**: Dimensionality Reduction / Anomaly Detection
- **Use Case**: Image compression, anomaly detection.
- **Idea**: Learns efficient codings of input data using neural networks.

---

## When to Use Unsupervised Learning?

- You have no labeled data available.
- You want to discover hidden patterns or structures.
- You aim to segment users, reduce noise, or visualize high-dimensional datasets.

---

## Summary

Unsupervised learning is a powerful tool for data exploration and structure discovery. It’s essential for tasks like clustering, anomaly detection, and reducing data dimensions. Understanding these methods helps in organizing and understanding raw datasets before further processing or modeling.
