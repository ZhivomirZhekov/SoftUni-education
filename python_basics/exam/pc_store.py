cpu_price = float(input())
gpu_price = float(input())
ram = float(input())
qty_ram = int(input())
discount = float(input())

cpu_price_bgn = cpu_price * 1.57
gpu_price_bgn = gpu_price * 1.57
ram_bgn = ram * 1.57
cpu_discount = cpu_price_bgn - (cpu_price_bgn * discount)
gpu_discount = gpu_price_bgn - (gpu_price_bgn * discount)


total = (cpu_discount + gpu_discount + ram_bgn * qty_ram)


print(f"Money needed - {total:.2f} leva.")
