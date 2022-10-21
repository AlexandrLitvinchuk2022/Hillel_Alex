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