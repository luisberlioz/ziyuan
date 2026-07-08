
-- DEFINICIONES DE TIPOS INDUCTIVOS

 inductive Bul : Type
  | falso : Bul
  | verdad : Bul

#check Bul.falso

def negar (b : Bul) : Bul :=
  match b with
  | .falso => Bul.verdad
  | .verdad => Bul.falso

def niega : Bul → Bul
  | .falso => Bul.verdad
  | .verdad => Bul.falso

#check Bul.falso

inductive dia : Type
  | domingo : dia
  | lunes : dia
  | martes : dia
  | miércoles : dia
  | jueves : dia
  | viernes : dia
  | sábado : dia

def dia_de_la_semana (d : dia) : Nat :=
  match d with
  | .domingo => 1
  | .lunes => 2
  | .martes => 3
  | .miércoles => 4
  | .jueves => 5
  | .viernes => 6
  | .sábado => 7

#eval dia_de_la_semana dia.domingo

------------------------------------------------------

-- slide 7
theorem not_involutive : ∀ b : Bool, not (not b) = b := by
  intro b
  cases b with
  | false => rfl
  | true => rfl

-- Demuestre este mismo teorema pero con el tipo Bul

------------------------------------------------------

-- slide 10
example (n : Nat) : n = n := by
  induction n with
  | zero => rfl
  | succ n ih => rw [ih]
-- Encuentre otras formas de probar el caso inductivo
-- usando apply?, simp?, etc.

------------------------------------------------------

-- slide 11
def predecesor : Nat → Nat
  | Nat.zero => Nat.zero
  | Nat.succ n => n

#eval predecesor 2026

------------------------------------------------------

-- slide 16
theorem add_zero : ∀m : Nat, m + 0 = m := by
  intro m
  rfl

theorem zero_add : ∀n : Nat, 0 + n = n := by
  intro n
  induction n with
  | zero => rfl
  | succ n ih => rw [Nat.add_left_comm]

---------------------------------------------------------

-- slide 17
theorem add_succ : ∀ m n : Nat, m + Nat.succ n = Nat.succ (m + n) := by
  intro m n
  induction m with
  | zero => rfl
  | succ m ih => rw [Nat.add_succ]

theorem succ_add : ∀m n : Nat, Nat.succ m + n = Nat.succ (m + n) := by
  intro m n
  induction n with
  | zero => rfl
  | succ n ih => rw [Nat.succ_add]
