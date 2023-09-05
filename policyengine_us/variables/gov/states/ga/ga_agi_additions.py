from policyengine_us.model_api import *


class ga_agi_additions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Georgia AGI additions to federal AGI"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://houpl.org/wp-content/uploads/2023/01/2022-IT-511_Individual_Income_Tax_-Booklet-compressed.pdf#page=14"
        "https://houpl.org/wp-content/uploads/2022/01/2021_IT-511_Individual_Income_Tax_Booklet-12.29.21-Web-Version.pdf#page=14"
    )
    defined_for = StateCode.GA