# Prompt Design Rationale

## Thought Process Behind Each Template

The four prompt templates were designed to support different needs in the e-commerce purchase prediction system. Each template has a clear purpose and focuses on a different type of output.

Template 1, Basic Prediction Explanation, was designed to explain the model prediction in a simple way. The goal is to help non-technical users understand why the model predicted Purchase or No Purchase.

Template 2, Marketing Recommendation Generator, was designed to turn the prediction into a practical business action. Instead of only explaining the result, this template suggests a suitable marketing response, such as a reminder or discount.

Template 3, Cluster-Based Personalized Explanation, was designed to make the explanation more personalized. It uses user behavior patterns from clustering, such as engagement level and browsing behavior, to explain the prediction in a more context-aware way.

Template 4, Safe and Responsible Explanation, was designed to avoid overconfident AI responses. It presents the prediction carefully and reminds the user that the result is based only on available session data.

## How Domain Knowledge Influenced Design

The prompt design was influenced by the Online Shoppers Intention dataset and the goal of predicting whether a user session will lead to a purchase. The dataset includes important e-commerce behavior features such as PageValues, BounceRates, ExitRates, ProductRelated, ProductRelated_Duration, VisitorType, Weekend, and Revenue.

These features helped guide the wording of the templates. For example, BounceRates and ExitRates were used as indicators of user engagement, while PageValues was treated as an important signal related to purchase intent. ProductRelated and ProductRelated_Duration helped describe how much the user interacted with product pages.

The templates were also designed to match the system goal: predicting purchase intention and making the result understandable. Therefore, the prompts focus on explanation, marketing action, personalization, and responsible communication.
