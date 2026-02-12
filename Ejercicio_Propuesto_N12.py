class EmployeeSalary:
	@staticmethod
	def calcular_salario(hours=48, rate=5000, retention_pct=12.5):
		salario_bruto = hours * rate
		retencion = salario_bruto * (retention_pct / 100.0)
		salario_neto = salario_bruto - retencion
		return salario_bruto, retencion, salario_neto


def main():
	horas = 48.0
	tarifa = 5000.0
	salario_bruto, retencion, salario_neto = EmployeeSalary.calcular_salario(horas, tarifa)
	
	print(f"Salario bruto: {salario_bruto:,.2f}")
	print(f"Retención ({12.5}%): {retencion:,.2f}")
	print(f"Salario neto: {salario_neto:,.2f}")


if __name__ == "__main__":
	main()