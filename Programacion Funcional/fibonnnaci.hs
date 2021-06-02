fibonnaci :: Int -> Int
fibonnaci 0=0
fibonnaci 1=1
fibonnaci num= fibonnaci (num-1) + fibonnaci (num-2)
serie :: Int -> [Int]
serie nu= map fibonnaci [1..nu]