import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Archimedean.Real.Basic
import Mathlib.Tactic.Basic
import Mathlib.Tactic.NormNum.Core

-----------------------------
-- DIA 2 LOGICA PROPOSICIONAL
-----------------------------

-- slide 3
variable (P Q : Prop)
#check P
#check P ∧ Q
#check P → Q

-- slide 5
example (P Q : Prop) (hq : Q) : P → Q :=
  fun (hp : P) => hq  -- elimine la sugerencia del Linter
-- demuestre
example (hq : B) : A → B :=
  sorry

-----------------------------------------------------

-- slide 6
-- intro de la conjuncion
example (a : A) (b : B) : A ∧ B := And.intro a b
-- elim de la conjuncion
example (hab : A ∧ B) : A := hab.1
-- intro de la disyuncion
example (a : A) : A ∨ B := Or.inl a
example (b : B) : A ∨ B := Or.inr b
-- elim de la disyuncion (hay varias formas de hacerlo)
example (P Q : Prop) (h : P ∨ Q) (hn : ¬P) : Q :=
  Or.elim h (fun hp => (hn hp).elim) (fun hq => hq)

-----------------------------------------------------

-- slide 7
-- si y solo si
example (P Q : Prop) (hp : P) (hq : Q) : P ↔ Q :=
  Iff.intro (fun _ => hq)  -- P → Q
            (fun _ => hp)  -- Q → P

-- Usando el ejemplo anterior, demuestre: P → Q
example (P Q : Prop) (hp : P) (hq : Q) : P → Q :=
  sorry

-- Negacion
example (P : Prop) (hn : ¬P) : ¬P := fun h : P => hn h

-----------------------------------------------------

-- slide 12
-- modo termino
example (P Q : Prop) (h : P ∧ Q) : Q ∧ P :=
  And.intro h.right h.left

-- modo tactico
example (P Q : Prop) (h : P ∧ Q) : Q ∧ P := by
  apply And.intro
  · exact h.right
  · exact h.left

example (P Q : Prop) (h : P ∧ Q) : Q ∧ P := by
  rw [and_comm] -- rescribimos el objetivo
  exact h

-- demuestre
-- El nombre analogo de "and_comm" para la disyuncion es...
example (P Q : Prop) (h : P ∨ Q) : Q ∨ P := by
  sorry

-----------------------------------------------------

-- comparacion de elim de disyuncion Termino vrs Tactico
example (P Q : Prop) (h : P ∨ Q) (hn : ¬P) : Q :=
  Or.elim h (fun hp => (hn hp).elim) (fun hq => hq)

example (P Q : Prop) (h : P ∨ Q) (hn : ¬P) : Q := by
  cases h with
  | inl hp => exact (hn hp).elim  -- uso contradiccion
  | inr hq => exact hq            -- hq es exactamente lo que quiero

-----------------------------------------------------

-- Probando ¬False
example : ¬False := fun f : False => f.elim

-----------------------------------------------------

-- slide 17
example (P Q R : Prop) (h1 : P) (h2 : P → Q) (h3 : Q → R) : R := by
  apply h3 -- meta: Q
  apply h2 -- meta: P
  exact h1 -- cierra: h1 : P

-----------------------------------------------------

-- slide 18
example (P Q R : Prop) (h : P ∨ Q) (hp : P → R) (hq : Q → R) : R := by
  cases h with
  | inl hp' => exact hp hp'
  | inr hq' => exact hq hq'

-----------------------------------------------------

-- slide 19
example (P Q : Prop) (hP : P) (hQ : Q) : P ∧ Q := by
 exact ⟨hP, hQ⟩

-- demuestre la commutatividad de la conjuncion
-- pero usando ⟨⬝ , ⬝⟩
example (P Q : Prop) (h : P ∧ Q) : Q ∧ P := by
 sorry

example (P Q : Prop) (h : P ∧ Q) : P := by
 exact h.1

-----------------------------------------------------

-- slide 21 - 23
example : ∀x : ℝ , x ≥ 0 → x = |x| := by
  intro x hnx
  -- tenemos que usar resultados de Mathlib
  exact Eq.symm (abs_of_nonneg hnx)

example : ∃ x : ℝ, 2 < x ∧ x < 3 := by
  use 5 / 2;
  -- tactica de mathlib
  norm_num

example : ∃ n : ℕ, 24 = 2 * n := by
  sorry


-----------------------------------------------------

-- slide 24
example (h : ∃ x : ℝ, x > 0) : True := by
  rcases h with ⟨w, hw⟩
-- ahora w : R y hw : w > 0 están en el contexto
  trivial

-----------------------------------------------------

-- slide 25
def CotaSup (f : ℝ → ℝ) (a : ℝ) : Prop := ∀ x, f x ≤ a

example (f g : ℝ → ℝ) (a b : ℝ)
-- example funciona, se puede inferir f g a b
  (hfa : CotaSup f a) (hgb : CotaSup g b) :
  CotaSup (fun x ↦ f x + g x) (a + b) := by
  intro x
  dsimp
  apply add_le_add
  · exact hfa x
  · exact hgb x


example (ubf : ∃ a, CotaSup f a) (ubg : ∃ b, CotaSup g b) :
          (∃c, CotaSup (fun x ↦ f x + g x) c) := by
  rcases ubf with ⟨a₀, ubfa⟩
  rcases ubg with ⟨b₀, ubgb⟩
  use a₀ + b₀
  intro x
  dsimp
  apply add_le_add
  · exact ubfa x
  · exact ubgb x

def monotona (f : ℝ → ℝ) : Prop :=
    ∀⦃a b⦄, a ≤ b →f a ≤ f b

----------------------------------------

-- #min_imports in norm_num
