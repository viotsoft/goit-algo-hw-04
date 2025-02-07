### **Висновки по алгоритмам сортування**

![image](https://github.com/user-attachments/assets/6f3ccb5e-ce3d-4a4a-904e-460ae38f79ca)


1. **Merge Sort (Сортування злиттям):**
   - **Переваги:**
     - Має стабільну продуктивність **O(n log n)** у всіх випадках (найкращий, середній, найгірший).
     - Підходить для сортування великих наборів даних.
   - **Недоліки:**
     - Потребує додаткової пам’яті для злиття підмасивів.
     - Виконується повільніше, ніж Timsort, для невеликих або частково впорядкованих даних.
   - **Висновок:** 
     - Алгоритм є гарним вибором для великих, невпорядкованих масивів, де стабільність і продуктивність важливі, але Timsort його перевершує в більшості практичних сценаріїв.

2. **Insertion Sort (Сортування вставками):**
   - **Переваги:**
     - Простий у реалізації.
     - Ефективний для малих або майже впорядкованих наборів даних (найкращий випадок – **O(n)**).
   - **Недоліки:**
     - Має низьку продуктивність **O(n²)** для великих або хаотичних наборів даних.
     - Стає непридатним для використання, якщо кількість елементів значно збільшується.
   - **Висновок:** 
     - Підходить лише для невеликих масивів або попередньо впорядкованих даних. Використовується як частина Timsort для обробки дрібних підмасивів.

3. **Timsort (Вбудований алгоритм Python):**
   - **Переваги:**
     - Поєднує переваги сортування злиттям та вставками.
     - Складність у найгіршому випадку – **O(n log n)**.
     - Особливо ефективний на частково впорядкованих даних (реальні сценарії).
     - Використовує сортування вставками для невеликих підмасивів і сортування злиттям для великих наборів.
   - **Недоліки:**
     - У деяких теоретичних випадках може мати додаткові витрати пам’яті (але це рідкість).
   - **Висновок:** 
     - Це найкращий вибір для реальних задач завдяки адаптивності та оптимізації. Використовується у вбудованих функціях Python (`sorted()` та `list.sort()`), тому програмісти зазвичай обирають саме його.

---

### **Загальний висновок**
- **Timsort** є найбільш оптимальним алгоритмом серед розглянутих для реальних сценаріїв завдяки своїй адаптивності та ефективності.
- **Merge Sort** зберігає свою цінність для великих даних, але програє Timsort через додаткові витрати пам’яті.
- **Insertion Sort** залишається корисним лише як допоміжний алгоритм для невеликих наборів даних або підмасивів.

Програмісти повинні використовувати вбудовані функції Python (`sorted` або `list.sort`) для сортування в повсякденних завданнях, оскільки вони базуються на Timsort і забезпечують найкращу продуктивність та простоту у використанні.
