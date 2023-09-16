# Sale - Business Model

## Objective
1. Create a new field 'Business Model' in Sale Order (field is Required)
    <details>
    <summary>Required field business model inside sale.order</summary>
    
    ![required field business model](./img/business_model%20field%20required.png)
    ![field business model inside account.tax to be used for filter](./img/business_model%20in%20account.tax%20to%20filter.png)
    </details>
2. Without changing the Sale Order name, change the Sale Order display name to include short name of the business model e.g ([RT] - S0001)
    1. Retail - [RT]
    2. Corporate - [CORP]
    3. Subscription - [SUB]
    <details>
    <summary>Change display name to add business model short name</summary>

    ![add business model short name to a display name](./img/business_model%20field%20required.png)
    </details>
3. Create an option to group the Sale Orders by Business Model in the Quotations tree view
    <details>
    <summary>Sale Order can be groupped by business_model</summary>

    ![Group by business_model](./img/group_by%20business_model.jpg)
    </details>
4. In the Sale Order Line, implement a way so that the Odoo user can only choose from the predetermined set of taxes based on selected Business Model
    <details>
    <summary>Filter tax by business model</summary>

    ![Group by business_model](./img/filter%20tax%20by%20business_model.png)
    </details>