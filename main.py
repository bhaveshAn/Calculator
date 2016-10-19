import kivy
kivy.require('1.8.0')
from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 

class CalcGrid(GridLayout):
	def calculate(self,calculation):
		if calculation:
			try:
				self.display.text=str(eval(calculation))
			except:
				self.display.text="Error"
				

class CalculatorApp(App):
	def build(self):
		return CalcGrid()

CalcApp=CalculatorApp()
CalcApp.run()