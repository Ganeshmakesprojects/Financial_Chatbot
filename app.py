from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message')
    # Simple rule-based responses
    if "hello" in user_input.lower():
        response = "Hello! I can provide financial details like total revenue, net income etc. of companies like Apple, Tesla and Microsoft. \nHow can I assist you today?\n"
    elif "bye" in user_input.lower():
        response = "Goodbye! Have a great day!\n"
    elif user_input.lower() in rb_responses:
        response = rb_responses[user_input.lower()]+'\n'
    else:
        response = "I'm not sure how to respond to that.\n"
    
    return jsonify({'response': response})

if __name__ == '__main__':
    df = pd.read_excel("Companies_3year_data.xlsx", index_col="Company")
    df = df.sort_values(by=['Company', 'Year'], ascending=True)
    rb_responses = {'what is the total revenue' : "Total Revenue of Apple in 2023 is {} mn $.".format(df[(df.Year == 2023)].loc["Apple", "Total Revenue"]),
                    'what is the total revenue of apple' : "Total Revenue of Apple in 2023 is {} mn $.".format(df[(df.Year == 2023)].loc["Apple", "Total Revenue"]),
                    'what is the total revenue apple in 2023' : "Total Revenue of Apple in 2023 is {} mn $.".format(df[(df.Year == 2022)].loc["Apple", "Total Revenue"]),
                    'what is the total revenue apple in 2022' : "Total Revenue of Apple in 2022 is {} mn $.".format(df[(df.Year == 2022)].loc["Apple", "Total Revenue"]),
                    'what is the total revenue apple in 2021' : "Total Revenue of Apple in 2021 is {} mn $.".format(df[(df.Year == 2021)].loc["Apple", "Total Revenue"]),
                    'what is the total profit of apple' : "Total Profit of Apple in 2023 is {} mn $.".format(df[(df.Year == 2023)].loc['Apple', 'Net Income']), 
                    'what is the total profit of apple in 2023' : "Total Profit of Apple in 2023 is {} mn $.".format(df[(df.Year == 2023)].loc['Apple', 'Net Income']),
                    'what is the total profit of apple in 2022' : "Total Profit of Apple in 2022 is {} mn $.".format(df[(df.Year == 2022)].loc['Apple', 'Net Income']), 
                    'what is the total profit of apple in 2021' : "Total Profit of Apple in 2021 is {} mn $.".format(df[(df.Year == 2021)].loc['Apple', 'Net Income']), 

                    'what is the total revenue of tesla' : "Total Revenue of Tesla in 2023 is {} mn $.".format(df[(df.Year == 2023)].loc["Tesla", "Total Revenue"]),
                    'what is the total revenue tesla in 2023' : "Total Revenue of Tesla in 2023 is {} mn $.".format(df[(df.Year == 2022)].loc["Tesla", "Total Revenue"]),
                    'what is the total revenue tesla in 2022' : "Total Revenue of Tesla in 2022 is {} mn $.".format(df[(df.Year == 2022)].loc["Tesla", "Total Revenue"]),
                    'what is the total revenue tesla in 2021' : "Total Revenue of Tesla in 2021 is {} mn $.".format(df[(df.Year == 2021)].loc["Tesla", "Total Revenue"]),
                    'what is the total profit of tesla' : "Total Profit of Tesla in 2023 is {} mn $.".format(df[(df.Year == 2023)].loc['Tesla', 'Net Income']), 
                    'what is the total profit of tesla in 2023' : "Total Profit of Tesla in 2023 is {} mn $.".format(df[(df.Year == 2023)].loc['Tesla', 'Net Income']),
                    'what is the total profit of tesla in 2022' : "Total Profit of Tesla in 2022 is {} mn $.".format(df[(df.Year == 2022)].loc['Tesla', 'Net Income']), 
                    'what is the total profit of tesla in 2021' : "Total Profit of Tesla in 2021 is {} mn $.".format(df[(df.Year == 2021)].loc['Tesla', 'Net Income']), 
                    
                    'what is the total revenue of microsoft' : "Total Revenue of Microsoft in 2023 is {} mn $.".format(df[(df.Year == 2023)].loc["Microsoft", "Total Revenue"]),
                    'what is the total revenue microsoft in 2023' : "Total Revenue of Microsoft in 2023 is {} mn $.".format(df[(df.Year == 2022)].loc["Microsoft", "Total Revenue"]),
                    'what is the total revenue microsoft in 2022' : "Total Revenue of Microsoft in 2022 is {} mn $.".format(df[(df.Year == 2022)].loc["Microsoft", "Total Revenue"]),
                    'what is the total revenue microsoft in 2021' : "Total Revenue of Microsoft in 2021 is {} mn $.".format(df[(df.Year == 2021)].loc["Microsoft", "Total Revenue"]),
                    'what is the total profit of microsoft' : "Total Profit of Microsoft in 2023 is {} mn $.".format(df[(df.Year == 2023)].loc['Microsoft', 'Net Income']), 
                    'what is the total profit of microsoft in 2023' : "Total Profit of Microsoft in 2023 is {} mn $.".format(df[(df.Year == 2023)].loc['Microsoft', 'Net Income']),
                    'what is the total profit of microsoft in 2022' : "Total Profit of Microsoft in 2022 is {} mn $.".format(df[(df.Year == 2022)].loc['Microsoft', 'Net Income']), 
                    'what is the total profit of microsoft in 2021' : "Total Profit of Microsoft in 2021 is {} mn $.".format(df[(df.Year == 2021)].loc['Microsoft', 'Net Income']), 
                   }
    app.run(debug=True)
    