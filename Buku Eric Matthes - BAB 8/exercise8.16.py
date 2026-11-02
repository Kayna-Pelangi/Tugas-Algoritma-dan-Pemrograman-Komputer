# 1. import module_name
import city_functions
city_functions.describe_city("bekasi")

# 2. from module_name import function_name
from city_functions import describe_city
describe_city("surakarta")

# 3. from module_name import function_name as fn
from city_functions import describe_city as dc
dc("tokyo", "Jepang")

# 4. import module_name as mn
import city_functions as cf
cf.describe_city("bandung")

# 5. from module_name import *
from city_functions import *
describe_city("osaka", "Jepang")