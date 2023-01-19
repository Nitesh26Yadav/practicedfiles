# guid = 'F36DF97E-F80C-44C1-A64F-6BE5D07FD298'
# UID = 1
# RuleId = 1



# getRuleCriteriaAndCoupon:-
#     f"exec ap_get_rule_criteria {RuleId}" 
#     f"exec ap_get_rule_products {RuleId}" 
#     f"exec ap_get_rule_departments {RuleId}"
#     f"exec ap_get_rule_offer {RuleId}"


# searchRules:-
#     body = {
#         "retailer": "1",
#         "ruletype":0,
#         "search": "",
#         "offset": 0,
#         "limit": 100,
#         "startdate": "",
#         "enddate": ""
#     }

#     f"exec ap_search_rules {body['retailer']}, {body['ruletype']}, '{body['search']}', '{body['startdate']}', '{body['enddate']}', 1, {body['offset']},{body['limit']},{UID}"

# GetRuleAnalysis, GetRulePerformance, GetRuleGroups:-
#     f"exec ap_get_rule '{RuleGuid}', {UID}"  

# GetRuleCriteriaUIConfig:-
#     f"exec ap_get_rule_criteria_ui_config {RuleType}, {SubRuleType}"

# ExpireRule:-
#     guid = '77B145BD-CD4D-489E-BF6F-E268E09A04F6'
#     f"exec ap_expire_rule '{guid}', {UID}"
#     f"exec ap_get_rule '{guid}', {UID}" 

# Getrule:

#  f"exec ap_get_rule_stores {RuleId}" 
#  "exec ap_get_rule_top_n_shoppers 0" 
#  f"exec ap_get_rule '{guid}', {UID}" 


# deleterule:-
    # f"exec ap_delete_rule '{guid}',{UID}"

