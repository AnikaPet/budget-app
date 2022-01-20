-- zadatak1

-- izlistati ime filma i br razlicitih gradova ako je br > 5
SELECT f.Naslov, COUNT(DISTINCT b.Grad)
FROM film f
	INNER JOIN projekcija p
		ON f.FID = p.FID 
	INNER JOIN bioskop b
		ON p.BID = b.BID
GROUP BY f.FID
HAVING COUNT(DISTINCT b.Grad) > 5;

-- film koji je imao najveci br projekcija

SELECT FID, COUNT(*) AS broj
FROM projekcija
GROUP BY FID
ORDER BY broj DESC LIMIT 1;

-- film koji je imao projekciju u svakom bioskopu

SELECT p.FID, COUNT(DISTINCT p.BID)
FROM projekcija p
GROUP BY p.FID
HAVING COUNT(DISTINCT p.BID) = (SELECT COUNT(*) FROM bioskop);

-- parovi filmova koji su projektovani u istim salama

SELECT p1.FID, p2.FID
FROM projekcija AS p1, projekcija AS p2
WHERE p1.BID = p2.BID;

-- gradovi u kojima se prikazivao film s najvecim br projekcija
SELECT b.Grad
FROM (SELECT FID, COUNT(*) AS broj
      FROM projekcija
      GROUP BY FID
      ORDER BY broj DESC LIMIT 1;) AS t1,
      projekcija AS p
      	INNER JOIN bioskop b 
      		ON b.BID = p.BID
WHERE t1.FID = p.FID;

-- FID,BID tako da je FID prikazan bar 3 puta u BID

SELECT FID,BID,COUNT(*)
FROM projekcija
GROUP BY FID,BID
HAVING COUNT(*) >= 3;

-- naci grad u kom je odrzana najposjecenija projekcija
SELECT b.Grad
FROM bioskop b, (SELECT BID
		  FROM projekcija p 
		  WHERE BrojGledalaca = (SELECT MAX(BrojGledalaca) FROM projekcija) AS t1
WHERE b.BID = t1.BID;

-- naci film koji je bio u svakoj sali bar dva puta

SELECT FID,COUNT(*)
FROM projekcija
GROUP BY FID,Broj
HAVING COUNT(*) > 2;

-- naci gradove dje su prikazani svi filmovi

SELECT b.Grad, COUNT(DISTINCT FID) AS br_filmova
FROM projekcija p
	INNER JOIN bioskop b
		ON p.BID = b.BID
GROUP BY b.Grad
HAVING broj_filmova = (SELECT COUNT(*) FROM film);

-- naci salu sa najvise posjetilaca

SELECT Broj, SUM(BrojGledalaca) AS suma
FROM projekcija
GROUP BY Broj
ORDER BY suma DESC LIMIT 1;

-- zadatak2

-- naci sale ciji je kapacitet > 50

SELECT *
FROM sala
WHERE kapacitet > 50; 

-- naci najvecu salu

SELECT * 
FROM sala
WHERE kapacitet = (SELECT MAX(kapacitet) FROM sala); 

--naci bioskope koji imaju vise od 1 sale	
					
SELECT b.BID, COUNT(*)
FROM bioskop AS b, sala AS s
WHERE b.BID = s.BID
GROUP BY b.BID
HAVING COUNT(*) > 1;

--naci filmove gdje je svaka projekcija imala > 50 gledalaca

SELECT p1.FID
FROM (
	SELECT FID, COUNT(*) AS cnt
	FROM projekcija
	GROUP BY FID ) as p1,
	(
	SELECT FID, COUNT(*) AS cnt
	FROM projekcija
	GROUP BY FID
	HAVING BrojGledalaca > 50 ) as p2
WHERE p1.FID = p2.FID AND p1.cnt = p2.cnt;

-- naci filmove koji su makar jednom projektovani u svakom bioskopu 

SELECT p.FID, COUNT(DISTINCT p.BID)
FROM projekcija p
GROUP BY p.FID
HAVING COUNT(DISTINCT p.BID) = (SELECT COUNT(*) FROM bioskop);
