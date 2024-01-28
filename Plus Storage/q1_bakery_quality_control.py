'''
-----------------------------------------------------------------------
File: q1_bakery_quality_control.py
Creation Time: Jan 27th 2024, 10:13 pm
Author: Aakash Vashishtha
Developer Email: 
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''

def pastry_quality_control(boxes_templates):
    def is_valid(box, template):
        box_count = {}
        template_count = {}

        for item in box:
            box_count[item] = box_count.get(item, 0) + 1

        for item in template:
            template_count[item] = template_count.get(item, 0) + 1

        return box_count == template_count

    invalid_count = 0

    for box, template in boxes_templates:
        if not is_valid(box, template):
            invalid_count += 1

    return invalid_count

# Example usage:
# boxes_templates_list = [
#     ["cm", "mc"],
#     ["ccm", "mc"],
#     ["pm", "mc"],
#     ["c", "mc"]
# ]

boxes_templates_list = [
    ["dmcd", "dcdmd"],
    ["k", "kkkkb"],
    ["k", "k"],
    ["pcmmcpp", "ppmc"],
    ["dmcd", "mdcd"]
]

result = pastry_quality_control(boxes_templates_list)
print(result)  # Output should be 3