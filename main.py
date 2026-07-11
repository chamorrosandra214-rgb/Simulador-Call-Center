import simpy
import random

# Función que simula la atención de un cliente
def cliente(env, nombre, agentes, tiempos):
    print(f"{nombre} llegó en el minuto {env.now}")

    with agentes.request() as solicitud:
        yield solicitud

        print(f"{nombre} está siendo atendido en el minuto {env.now}")

        tiempo_atencion = random.randint(3, 8)
        tiempos.append(tiempo_atencion)

        yield env.timeout(tiempo_atencion)

        print(f"{nombre} terminó su llamada en el minuto {env.now}")

# Generador de clientes
def generar_clientes(env, total_clientes, agentes, tiempos):
    for i in range(total_clientes):
        env.process(cliente(env, f"Cliente {i+1}", agentes, tiempos))
        yield env.timeout(random.randint(1, 3))

# Programa principal
def main():
    print("===== SIMULADOR DE CALL CENTER =====")

    total_clientes = int(input("Ingrese el número de clientes: "))
    numero_agentes = int(input("Ingrese el número de agentes: "))

    env = simpy.Environment()
    agentes = simpy.Resource(env, capacity=numero_agentes)

    tiempos = []

    env.process(generar_clientes(env, total_clientes, agentes, tiempos))
    env.run()

    promedio = sum(tiempos) / len(tiempos)

    print("\n===== RESULTADOS =====")
    print("Número de llamadas:", total_clientes)
    print("Número de clientes:", total_clientes)
    print("Clientes atendidos:", len(tiempos))
    print("Tiempo promedio de atención:", round(promedio, 2), "minutos")

if __name__ == "__main__":
    main()
    
