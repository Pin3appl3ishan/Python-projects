from dataclasses import dataclass

@dataclass
class Prediction:
    value: float  # predicted value
    r2_score: float # co-efficient of determination, measuring goodness of fit of the model
    slope: float    # slope of regression line
    intercept: float    # y-intercept of regression line
    mean_absolute_error: float  # average absolute diff- between predicted and actual values

    def __str__(self):
        # displays the predicted value with two decimal places and r2_score as a percentage
        return f'Prediction: {self.value:.2f} ({self.r2_score:.2%})'