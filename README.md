## Django port => 8000 [CORS enables for frontend]
## React Port => 3000 

## API Endpoints
  ### api/  [Public Endpoints]
  
  * `get-gross-pay/<int:employee_id>` [GET]
    * GET request to get the gross pay per month [Without Tax deduction] -> Needs `employee_id` as a path parameter
   
      
  * `get-net-pay/<int:employee_id>/<slug:month>` [GET]
    * GET request to get the net pay [With Tax deduction] -> Needs `employee_id` as a path parameter.
   
 ### api/  [Private  Endpoints]
 
  * `add-employee-basic-pay-of-month` [POST]
    * Adds employee basic payment to database 
      * Request Body anatomy - `{
    "employee_id":333,
    "employee_pay_scale":20000
}`

  * `add-employee-tax` [POST]
     * Adds employee tax info to database 
       * Request Body anatomy - `{
    "employee_id":555,
    "employee_tax":23
}`

  * `add-employee-attendance-for-month` [POST]
     * Adds employee monthly attendace info to database 
       * Request Body anatomy - `{
    "days_present":21,
    "employee_id":333,
    "month":"June"
}`

Database at a glance :
![Screenshot (3663)](https://github.com/damodar-d/payroll_dashboard/assets/79585993/40643f13-a285-4da9-99e0-bbefceafc03e)
