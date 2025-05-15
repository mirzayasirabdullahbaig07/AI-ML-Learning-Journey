# Reinforcement Learning

## What is Reinforcement Learning?

Reinforcement Learning (RL) is a type of machine learning where an agent learns to make decisions by interacting with an environment. It learns from feedback in the form of **rewards** or **penalties**, aiming to maximize cumulative reward over time.

Unlike supervised or unsupervised learning, reinforcement learning is based on trial and error.

---

## Key Concepts in Reinforcement Learning

- **Agent**: The learner or decision maker.
- **Environment**: The world the agent interacts with.
- **State (S)**: A representation of the current situation.
- **Action (A)**: A set of possible moves the agent can take.
- **Reward (R)**: Feedback from the environment for an action.
- **Policy (π)**: Strategy that the agent follows to choose actions.
- **Value Function (V)**: Expected long-term return of states.

---

## Reinforcement Learning Process

1. Agent observes the **current state** of the environment.
2. Agent chooses an **action** based on its policy.
3. Environment returns a **reward** and the **next state**.
4. Agent updates its strategy to improve future rewards.

This loop continues until the agent learns an optimal strategy.

---

## Important Reinforcement Learning Algorithms

### 1. Q-Learning
- **Type**: Model-free RL
- **Use Case**: Environments with discrete state and action spaces.
- **Idea**: Learns a value function that maps state-action pairs to expected rewards.

### 2. SARSA (State-Action-Reward-State-Action)
- **Type**: Model-free RL
- **Use Case**: Similar to Q-learning but considers the action taken in the next state.
- **Idea**: On-policy algorithm that updates values using the action actually taken.

### 3. Deep Q-Networks (DQN)
- **Type**: Deep Reinforcement Learning
- **Use Case**: Complex environments like video games.
- **Idea**: Combines Q-learning with deep neural networks for approximation.

### 4. Policy Gradient Methods
- **Type**: Policy-based RL
- **Use Case**: Continuous action spaces.
- **Idea**: Directly optimizes the policy instead of the value function.

### 5. Actor-Critic Methods
- **Type**: Hybrid RL
- **Use Case**: Stable learning in continuous environments.
- **Idea**: Uses two models — one for policy (actor) and one for value estimation (critic).

---

## When to Use Reinforcement Learning?

- You are working with environments where decisions affect future states.
- You need a model that improves through experience.
- You’re building agents for robotics, games, or control systems.

---

## Applications of Reinforcement Learning

- Game playing (e.g., AlphaGo, Dota 2 AI)
- Robotics and automation
- Recommendation systems
- Traffic light control
- Stock trading bots

---

## Summary

Reinforcement learning is a dynamic learning paradigm where agents learn optimal strategies through interaction. It is powerful for solving problems involving decision making, planning, and control — especially where learning from labeled data is not feasible.
