-- creates a trigger that decreases the quantity of an item after adding a new order.


-- Create the trigger
DELIMITER //

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - orders.number
    WHERE item_name = orders.name;
END //

DELIMITER ;