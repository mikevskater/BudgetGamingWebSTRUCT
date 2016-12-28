SELECT 
        item_name, 
        item_subtitle,
        item_category,
        item_condition,
        item_conditionDesc,
        item_cost
        FROM item 
                ORDER BY item_id 
                        DESC