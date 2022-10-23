avg_salary = 2040
qty_employees: int = 18
max_salary = 3500
min_salary = 1500
insurance_empl = 480
salary_budge = avg_salary * qty_employees

company_name = ('First IT Solution')
country_of_registration = ('Ukraine')
location_city = ('Kyiv')
director_fr_name = ('Robert')
director_ls_name = ('Li')

print('Company ' , company_name , ' is in ' , country_of_registration , ' in city ' , location_city + ".")
print('The company is managed ' + director_fr_name +' '+ director_ls_name + ".")
print('Total number of employees in ', company_name, '-', qty_employees, ' people.')
print("Average salary in ",company_name, avg_salary, "usd.")
print(director_fr_name, 'has Maximum salary',  ' - ',max_salary, "usd.")
print('Minimum salary', '-',min_salary, "usd." )
print('Company budget per month', '-',salary_budge, "usd.")
print('Employee insurance', '-',insurance_empl, "usd", ' per year.')
print('Total insurance budget - ', qty_employees*insurance_empl, "usd per year.")
###########################################################################
avg_salary_: int = 2040
qty_employees_: int = 18
max_salary_: int = 3500
min_salary_: int = 1500
insurance_empl_: int = 480
salary_budge_: int = avg_salary * qty_employees

company_name_:str = ('First IT Solution')
country_of_registration_:str = ('Ukraine')
location_city_:str = ('Kyiv')
director_fr_name_:str = ('Robert')
director_ls_name_:str = ('Li')

print(type(avg_salary_))
print(type(company_name_))
print(type(qty_employees_))
print(type(country_of_registration_))

print('AVG salary - ', int(avg_salary_))
print('QTY employees - ', int(qty_employees_))
print('Max salary - ', int(max_salary_))
print('Min salary - ', int(min_salary_))
print('Insurance empl - ', int(insurance_empl_))
print('Salary_budge - ', int(salary_budge_))

print('Company name - ', str(company_name_))
print('Country of registration - ', str(country_of_registration_))
print('Location city - ', str(location_city_))
print('Director name - ', str(director_fr_name_), str(director_ls_name_))