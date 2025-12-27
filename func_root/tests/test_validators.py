from PioneersVision.func_root.utils.validators import validate_text

# should pass
validate_text("Hello")

# should fail
try:
    validate_text("")
except ValueError as e:
    print("Caught error:", e)

try:
    validate_text(123)
except ValueError as e:
    print("Caught error:", e)
