from flask import Flask, render_template

app = Flask(__name__)

class Fizzbuzz:
    def __init__(self):
        self.fizzbuzz_list = [] #List should contain "Fizz", "Buzz", "FizzBuzz"

    def get_fizzbuzz(self):
        for num in range(1, 101):
            if num % 3 == 0 and num % 5 == 0:
                self.fizzbuzz_list.append('FizzBuzz')
            elif num % 3  == 0:
                self.fizzbuzz_list.append('Fizz')
            elif num % 5 == 0:
                self.fizzbuzz_list.append('Buzz')
            else:
                self.fizzbuzz_list.append(num)

@app.route('/fizzbuzz', methods=["GET"])
def fizzbuzz():
    fizzbuzz = Fizzbuzz()
    fizzbuzz.get_fizzbuzz()
    return render_template('new.html', fizzbuzz_list = fizzbuzz.fizzbuzz_list)


# This block of code is executed if the file is run as a script (not imported as a module)
if __name__ == '__main__':
    # Run the Flask web server with debugging mode turned on
    app.run(debug=True)