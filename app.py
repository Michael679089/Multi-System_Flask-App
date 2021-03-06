from flask import Flask, render_template, url_for, request, redirect

# Setting up the Application
app = Flask(__name__)

# ROUTE Function Application
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/DistanceConverter', methods=['POST', 'GET'])
def DistanceConverter():
    # Conversion of Distance Functions
    Mi = [  # 0 - km, 1 - cm, 2 - foot, 3 - in
        1.609344,
        160934,
        5280,
        63360
        ]

    KmMi = 0.621371
    KmCm = 10000
    KmFt = 3280.84
    KmIn = 39370.1

    CmKm = 0.00001
    CmMi = 0.0000062137
    CmFt = 0.0328084
    CmIn = 0.393701

    FtKm = 0.0003048
    FtCm = 30.48
    FtMi = 0.000189394
    FtIn = 12

    InKm = 0.0000254
    InCm = 2.54
    InMi = 0.0000157828
    InFt = 0.0833333
    
    ## Miles
    def Mi_To_Km(input):
        try:
            kilometer_output = float(input) * Mi[0]
            return round(kilometer_output, 2)
        except:
            print("ERROR: Input to Kilometer")
            return

    def Mi_To_Cm(input):
        try:
            kilometer_output = float(input) * Mi[1]
            return round(kilometer_output, 2)
        except:
            print("ERROR: Input to Kilometer")
            return

    def Mi_To_Ft(input):
        try:
            kilometer_output = float(input) * Mi[2]
            return round(kilometer_output, 2)
        except:
            print("ERROR: Input to Feet")
            return
    
    def Mi_To_In(input):
        try:
            kilometer_output = float(input) * Mi[3]
            return round(kilometer_output, 2)
        except:
            print("ERROR: Input to Inches")
            return

    ## Kilometers    
    def Ki_To_Mi(input):
        try:
            Miles_output = float(input) * KmMi
            return round(Miles_output, 2)
        except:
            print("ERROR: Input to Kilometer")
            return
    def Ki_To_Cm(input):
        try:
            Centimeter_Output = float(input) * KmCm
            return round(Centimeter_Output, 2)
        except:
            print("ERROR: Input to Kilometer")
            return
    def Ki_To_Ft(input):
        try:
            Feet_Output = float(input) * KmFt
            return round(Feet_Output, 2)
        except:
            print("ERROR: Input to Kilometer")
            return
    def Ki_To_In(input):
        try:
            Inches_Output = float(input) * KmIn
            return round(Inches_Output, 2)
        except:
            print("ERROR: Input to Inches")
            return

    ## Centimeters
    def Cm_To_Km(input):
        try:
            Kilometers_Output = float(input) * CmKm
            return round(Kilometers_Output, 2)
        except:
            print("ERROR: Input to Kilometer")
            return
    def Cm_To_Mi(input):
        try:
            Miles_Output = float(input) * CmMi
            return round(Miles_Output, 2)
        except:
            print("ERROR: Input to Kilometer")
            return
    def Cm_To_Ft(input):
        try:
            Feet_Output = float(input) * CmFt
            return round(Feet_Output, 2)
        except:
            print("ERROR: Input to Kilometer")
            return
    def Cm_To_In(input):
        try:
            Inches_Output = float(input) * CmIn
            return round(Inches_Output, 2)
        except:
            print("ERROR: Input to Inches")
            return
    
    ## Feet
    def Ft_To_Km(input):
        try:
            Feet_Output = float(input) * FtKm
            return round(Feet_Output, 2)
        except:
            print("ERROR: Input to Kilometer")
            return
    def Ft_To_Cm(input):
        try:
            Feet_Output = float(input) * FtCm
            return round(Feet_Output, 2)
        except:
            print("ERROR: Input to Kilometer")
            return
    def Ft_To_Mi(input):
        try:
            Miles_Output = float(input) * FtMi
            return round(Miles_Output, 2)
        except:
            print("ERROR: Input to Kilometer")
            return
    def Ft_To_In(input):
        try:
            Inches_Output = float(input) * FtIn
            return round(Inches_Output, 2)
        except:
            print("ERROR: Input to Inches")
            return

    ## Inches
    def In_To_Km(input):
        try:
            Kilometers_Output = float(input) * InKm
            return round(Kilometers_Output, 2)
        except:
            print("ERROR: Input to Kilometer")
            return
    def In_To_Cm(input):
        try:
            Centimeters_Output = float(input) * InCm
            return round(Centimeters_Output, 2)
        except:
            print("ERROR: Input to Centimeter")
            return
    def In_To_Mi(input):
        try:
            Miles_Output = float(input) * InMi
            return round(Miles_Output, 2)
        except:
            print("ERROR: Input to Miles")
            return
    def In_To_Ft(input):
        try:
            Feet_Output = float(input) * InFt
            return round(Feet_Output, 2)
        except:
            print("ERROR: Input to Feet")
            return

    # Data Gathering
    mile_input = 0
    input_distance = " "
    what_distance = " "
    convertedDistance = 0

    if request.method == 'POST':
        user_input = request.form.get("user_input")
        input_distance = request.form.get("input_distance")
        what_distance = request.form.get("what_distance")
        
        if (input_distance == 'Miles'):
            if (what_distance == "Kilometer"):
                convertedDistance = Mi_To_Km(user_input)
            elif (what_distance == "Centimeter"):
                convertedDistance = Mi_To_Cm(user_input)
            elif (what_distance == "Foot"):
                convertedDistance = Mi_To_Ft(user_input)
        elif(input_distance == "Kilometer"):
            if (what_distance == "Mile"):
                convertedDistance = Ki_To_Mi(user_input)
            elif (what_distance == "Centimeter"):
                convertedDistance = Ki_To_Cm(user_input)
            elif (what_distance == "Foot"):
                convertedDistance = Ki_To_Ft(user_input)
            elif (what_distance == "Inch"):
                convertedDistance = Ki_To_In(user_input)
        elif(input_distance == "Centimeter"):
            if (what_distance == "Kilometer"):
                convertedDistance = Cm_To_Km(user_input)
            elif (what_distance == "Mile"):
                convertedDistance = Cm_To_Mi(user_input)
            elif (what_distance == "Foot"):
                convertedDistance = Cm_To_Ft(user_input)
            elif (what_distance == "Inch"):
                convertedDistance = Cm_To_In(user_input)
        elif(input_distance == "Foot"):
            if (what_distance == "Kilometer"):
                convertedDistance = Ft_To_Km(user_input)
            elif (what_distance == "Centimeter"):
                convertedDistance = Ft_To_Mi(user_input)
            elif (what_distance == "Mile"):
                convertedDistance = Ft_To_Mi(user_input)
            elif (what_distance == "Inch"):
                convertedDistance = Ft_To_In(user_input)
        elif(input_distance == "Inch"):
            if (what_distance == "Kilometer"):
                convertedDistance = In_To_Km(user_input)
            elif (what_distance == "Centimeter"):
                convertedDistance = In_To_Mi(user_input)
            elif (what_distance == "Mile"):
                convertedDistance = In_To_Ft(user_input)
            elif (what_distance == "Foot"):
                convertedDistance = In_To_Ft(user_input)
        
        
        if (input_distance == what_distance):
            convertedDistance = user_input
        
    return render_template('DistanceConverter.html', convertedDistance=convertedDistance)

@app.route('/DoubleSquare_and_HalfANumber', methods=['POST', 'GET']) 
def DoubleSquare_and_HalfANumber():
    user_input = 0
    options = " "
    converted_input = 0

    if (request.method == 'POST'):
        try:
            user_input = int(request.form.get('user_input'))
            options = request.form.get('options')
        except ValueError:
            user_input = 0

        if (options == "Double"):
            converted_input = user_input * 2
        elif (options == "Square"):
            converted_input = user_input ** 2
        elif (options == "Half"):
            converted_input = user_input / 2
        else:
            print("ERROR")

    return render_template('DoubleSquare_and_HalfANumber.html', converted_input = converted_input)
    
@app.route('/PintConverter', methods=['POST', 'GET'])
def PintConverter():
    user_input_pint = 0
    options = " "
    converted_input = 0

    PintTo = {
        "Gills" : 4,
        "Quarts" : 0.5,
        "Gallons" : 0.125
    }

    if request.method == 'POST':
        try:
            user_input_pint = int(request.form.get('user_input_pint'))
            options = request.form.get('options')
            converted_input = 0
        except ValueError:
            user_input_pint = 0

        if (options == 'Gill'):
            converted_input = user_input_pint * PintTo["Gills"]
        elif (options == 'Quart'):
            converted_input = user_input_pint * PintTo["Quarts"]
        elif (options == 'Gallon'):
            converted_input = user_input_pint * PintTo["Gallons"]

    return render_template('PintConverter.html', converted_input = converted_input)

@app.route('/PoundsToGrams', methods=['POST', 'GET'])
def PoundsToGrams():
    user_input_pounds = 0
    converted_output = 0
    user_input_pounds = 0

    if request.method == 'POST':
        user_input_pounds = request.form.get('user_input_pounds')

        try:
            converted_output = float(user_input_pounds) * 453.592
            converted_output = round(converted_output, 4)
        except ValueError:
            converted_output = 0



    return render_template('PoundsToGrams.html', converted_output = converted_output)
    

# Debug and Run
if __name__ == '__main__':
    app.run(debug=True)


