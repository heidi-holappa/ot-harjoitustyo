# Week 3 - Task 4: Sequence Diagram

```mermaid
sequenceDiagram
  participant main
  participant laitehallinto
  participant ratikka6
  participant bussi244
  participant rautatietori
  participant kallen_kortti
  participant lippu_luukku
  main ->> laitehallinto: lisaa_lataaja(rautatientori)
  main ->> laitehallinto: lisaa_lukija(ratikka6)
  main ->> laitehallinto: lisaa_lukija(bussi244)
  main ->> lippu_luukku: osta_matkakortti("Kalle")
  activate lippu_luukku
  lippu_luukku ->> kallen_kortti: Matkakortti("Kalle")
  deactivate lippu_luukku
  main ->> rautatietori: lataa_arvoa(kallen_kortti, 3)
  activate rautatietori
  rautatietori ->> kallen_kortti: kasvata_arvoa(3)
  deactivate rautatietori
  main ->> ratikka6: osta_lippu(kallen_kortti, 0)
  activate ratikka6
  ratikka6 ->> kallen_kortti: kallen_kortti.arvo
  ratikka6 ->> kallen_kortti: vahenna_arvoa(1.5)
  ratikka6 -->> main: True
  deactivate ratikka6
  main->> bussi244: osta_lippu(kallen_kortti, 2)
  activate bussi244
  bussi244 ->> kallen_kortti: kallen_kortti.arvo
  bussi244 -->> main: False
  deactivate bussi244
```

## Comments
Based on the example in the course material I made the assumption that it is not necessary to include the creation of objects and their classes to the sequence diagram. I personally think they could be beneficial for easier reading in some cases, but in this case it is easy to see from the methods called what classes different objects represent. 

One this I struggled with were the conditions in methods. For example in the method call *osta_lippu(kallen_kortti, 0)* a conditional check is done to see if there is enough balance to buy a ticked. I made the decision to include the check for the balance (*kallen_kortti.arvo*) and the method call that followed from the condition being true and the return of value **True** to the main.
