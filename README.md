# Sale - Business Model

## Objective
1. Create a new field 'Business Model' in Sale Order (field is Required)
    - field business_model is required in sale.order model
    ![required field business model](./img/business_model%20field%20required.png)
    - field business_model inside account.tax to be used for filtering
    ![field business model inside account.tax to be used for filter](./img/business_model%20in%20account.tax%20to%20filter.png)
3. Without changing the Sale Order name, change the Sale Order display name to include short name of the business model e.g ([RT] - S0001)
    1. Retail - [RT]
    2. Corporate - [CORP]
    3. Subscription - [SUB]
    
    Change display name to add business model short name
    ![add business model short name to a display name](./img/business_model%20field%20required.png)
4. Create an option to group the Sale Orders by Business Model in the Quotations tree view
    
    Group by business_model
    ![Group by business_model](./img/group_by%20business_model.jpg)
6. In the Sale Order Line, implement a way so that the Odoo user can only choose from the predetermined set of taxes based on selected Business Model
    
    Show tax with the same business model
    ![Group by business_model](./img/filter%20tax%20by%20business_model.png)
