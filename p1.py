class rectangulo(): ##Pedira los datos del rectangulo
    b_r = float(input("Medida de la base del rectangulo: "))
    alt = float(input("Altura del del prisma/piramide: "))
    alt_r = float(input("Altura del rectangulo: "))
    def pr(self, vol, area_r, alt_r):
        vol = area_r * alt_r
        return vol
    def piram_r(self, vol_pir, area_r, alt_r):
        vol_pir = (area_r * alt_r) / 3
        return vol_pir
    def a_r(self, area_r, b_r, alt_r):
        area_r = b_r * alt_r
        return area_r
 
class triangulo(): ##Pedira los datos del triangulo
    alt_t = float(input("Medida de la altura del prisma: "))
    b_t = float(input("Medida de la base del triángulo: "))
    alt_t = float(input("Medida de la altura del triángulo: "))
    def pr_t(self, area_t, alt_t, prismat):
        prismat = area_t * alt_t
        return prismat
    def a_t(self, b_t, alt_t, area_t):
        area_t = (b_t * alt_t) / 3
        return area_t
    def pir_t(self, area_r, alt_r, v_pit):
        v_pit = (area_r * alt_r) / 3

class circulo(): ##Pedira los datos del circulo
    rad = float(input("Medida del radio de la base: "))
    alt = float(input("Medida de la altura del prisma: "))
    a = 0
    pi = 3.1416
    def piramide(self, v_pi, area, alt):
        v_pi = area * alt
        return v_pi
    def area(self, rad, pi):
        area = (pi)(rad**2)
        return area
    def prisma(self, vol, area, alt):
        vol = area * alt
        return vol