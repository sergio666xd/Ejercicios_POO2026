class Numero:
	@staticmethod
	def cuadrado_cubo(n):
		return n ** 2, n ** 3


def main():
	entrada = input("Ingrese un número: ")
	n = float(entrada)
	sq, cube = Numero.cuadrado_cubo(n)
	print(f"Número: {n:.0f}")
	print(f"Cuadrado: {sq:.0f}")
	print(f"Cubo: {cube:.0f}")


if __name__ == "__main__":
	main()