# Convert seconds into hours, minutes and seconds.
total_sec = int(input("Enter seconds:"))
hrs = total_sec//3600
remaining_sec = total_sec%3600
minutes = remaining_sec//60
seconds = remaining_sec%60
print(f"{hrs} hrs, {minutes} min, {seconds} sec")