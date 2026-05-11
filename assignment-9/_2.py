# 2. Hospital Emergency Priority System

# A hospital assigns treatment priority based on age, severity, and insurance.

# If severity is critical, then check age. If age is 60 or above, assign Immediate ICU; otherwise assign Emergency Ward.

# If severity is moderate, then check insurance. If insured, assign Priority Treatment; otherwise assign General Queue.

# If severity is low, then check age. If age is less than 10, assign Pediatric Priority; otherwise assign Wait.

# Input:
# Age = 65
# Severity = critical
# Insurance = yes

# Output:
# Treatment = Immediate ICU

age      = int(input("Enter age: "))
severity = input("Enter severity: ").lower()
insured  = input("Insurance (yes/no): ").lower()

if severity == "critical":
    if age >= 60:
        treatment = "Immediate ICU"
    else:
        treatment = "Emergency Ward"
else:
    if severity == "moderate":
        if insured == "yes":
            treatment = "Priority Treatment"
        else:
            treatment = "General Queue"
    else:
        if age < 10:
            treatment = "Pediatric Priority"
        else:
            treatment = "Wait"

print("Treatment =", treatment)