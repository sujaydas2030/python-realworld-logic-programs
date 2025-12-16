#Job Role Predictor
# Taking the input 
user_input = input()

# Convert input string to list of integers
values = [int(x.strip()) for x in user_input.split(',')]

# Write your code here
# Define skill names in order
skills=['communication','problem_solving','technical_knowledge','creativity','leadership']

# Create a dictionary mapping skills to their ratings
map_dic=dict(zip(skills,values))

# Define the prediction function
def predict_job_role(map_dic):
    # Write your code here
    comm=map_dic['communication']
    prob_sol=map_dic['problem_solving']
    tech=map_dic['technical_knowledge']
    crea=map_dic['creativity']
    lead=map_dic['leadership']
    if tech>=4 and prob_sol>=4 and comm<=3:
        return 'Software Developer'
    elif comm>=4 and lead>=4 and prob_sol>=3:
        return 'Product Manager'
    elif crea>=4 and comm>=3 and tech<=3:
        return 'UX Designer'
    elif tech>=4 and prob_sol>=4 and lead<=3:
        return 'Data Analyst'
    elif comm>=4 and lead>=3 and crea>=3:
        return 'Sales Executive'
    else:
        return "Product Manager"
# Print the output for the predicted job role
print(predict_job_role(map_dic))
