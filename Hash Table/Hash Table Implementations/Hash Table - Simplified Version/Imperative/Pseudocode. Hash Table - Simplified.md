```
// HASH TABLE CODE INSPIRED BY CAMBRIDGE BOOK BY SYLVIA LANGFIELD
DECLARE hash_table : ARRAY [0:9] OF INTEGER
```
```
FUNCTION hash_function(Key) RETURNS INTEGER
    Address ← Key MOD LENGTH(hash_table)
    RETURN Address
END FUNCTION
```
```
PROCEDURE insert(Key)
    Index ← hash_function(Key)
    WHILE hash_table[Index] <> 0
        Index ← (Index + 1) MOD LENGTH(hash_table)
    END WHILE
    hash_table[Index] ← Key
END PROCEDURE
```
```
FUNCTION search(Key) RETURNS INTEGER
    Index ← hash_function(Key)
    WHILE hash_table[Index] <> Key
        Index ← (Index + 1) MOD LENGTH(hash_table)
        IF hash_table[Index] = 0 THEN
            RETURN -1
        END IF
    END WHILE
    RETURN Index
END FUNCTION
```
```
# Main program starts here
DECLARE keys: ARRAY [0:4] AS INTEGER
keys ← [45876, 32390, 95312, 64636, 23467]

FOR i ← 0 TO LENGTH(keys) - 1
    CALL insert(keys[i])
NEXT

INPUT "Enter the search key: ", search_key
found_index ← CALL search(search_key)

IF found_index = -1 THEN
    OUTPUT "Key not found."
ELSE
    OUPUT "Key found at index", found_index
END IF

FOR i ← 0 TO LENGTH(hash_table) - 1
    OUTPUT hash_table[i]
NEXT
```