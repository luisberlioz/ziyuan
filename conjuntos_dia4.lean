import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Algebra.Order.Archimedean.Real.Basic
import Mathlib.Topology.Filter
import Mathlib.Topology.Defs.Filter
import Mathlib.Topology.Order.Basic
import Mathlib.Topology.MetricSpace.Basic
import Mathlib.Tactic


open Set

-- slide 7
-- Even n significa que existe un m tal que n = m + m
def evens : Set ℕ := { n | Even n }

def odds : Set ℕ := { n | ¬ Even n }

def positives : Set ℝ := { x | 0 < x }

-- rfl hace un poco mas que solo la prop reflexiva
example : 2 + 2 = 4 := rfl

example : 4 ∈ evens := by exact ⟨2, rfl⟩
example : 10 ∈ evens := sorry

example : 5 ∉ evens := by
  rintro ⟨n, h⟩
  have h' : 5 = 2 * n := by
    rw [Nat.two_mul]
    exact h
  have h'' : 5 % 2 = 0 := by
    rw [h', Nat.mul_mod_right]
  have h''' : 5 % 2 = 1 := rfl
  contradiction

example : 3 ∉ evens := sorry

example : 0 ∉ positives := by
  simp [positives]

-----------------------------------------------------------

-- slide 8
-- Creamos conjuntos de tipo Set α
-- Que es α? -- no importa, puede ser cualquier tipo.
variable {α : Type*} (s t : Set α)

example : s ∩ t = t ∩ s := by
  ext x
  simp only [mem_inter_iff]
  apply And.comm

example : s ∪ t = t ∪ s := by
  sorry

-----------------------------------------------------------

--slide 9
-- Probamos el mismo teorema de varias formas
example (h : s ⊆ t) : s ∩ u ⊆ t ∩ u := by
  intro x xsu
  exact ⟨h xsu.1, xsu.2⟩ -- estilo ``término''

example (h : s ⊆ t) : s ∩ u ⊆t ∩ u := by
  rintro x ⟨xs, xu⟩
  exact ⟨h xs, xu⟩ -- rintro destructura

example (h : s ⊆ t) : s ∩ u ⊆ t ∩ u := by
  rw [subset_def, inter_def, inter_def]
  rw [subset_def] at h
  simp only [mem_setOf]
  rintro x ⟨xs, xu⟩
  exact ⟨h _ xs, xu⟩ -- reescribiendo definiciones

example (h : s ⊆ t) : s ∪ u ⊆ t ∪ u := by
  intro x xsu
  cases xsu with
  | inl xs => exact Or.inl (h xs)
  | inr xu => exact Or.inr xu

------------------------------------------------------------

--slide 10
-- Distributividad de la intersección sobre la unión
example : s ∩ (t ∪ u) ⊆ s ∩ t ∪ s ∩ u := by
  rintro x ⟨xs, xt | xu⟩
  · left; exact ⟨xs, xt⟩
  · right; exact ⟨xs, xu⟩

example : s ∩ t ∪ s ∩ u ⊆ s ∩ (t ∪ u) := by
  rintro x (⟨xs, xt⟩| ⟨xs, xu⟩)
  · exact ⟨xs, Or.inl xt⟩
  · exact ⟨xs, Or.inr xu⟩

-- complete la demostración de la igualdad usando Iff.intro
example : s ∩ (t ∪ u) = s ∩ t ∪ s ∩ u := by
  ext x
  apply Iff.intro
  · rintro ⟨xs, xt | xu⟩
    · sorry
    · sorry
  · rintro (⟨xs, xt⟩ | ⟨xs, xu⟩)
    · sorry
    · sorry

-------------------------------------------------------------

--slide 11
-- diferencia de conjuntos
example : (s \ t) \ u ⊆ s \ (t ∪ u) := by
  rintro x ⟨⟨xs, xnt⟩, xnu⟩
  use xs
  rintro (xt | xu) <;> contradiction


example : s \ (t ∪u) ⊆(s \ t) \ u := by
  rintro x ⟨xs, hxtu⟩
  exact ⟨⟨xs, fun xt => hxtu (Or.inl xt)⟩,
  fun xu => hxtu (Or.inr xu)⟩

--------------------------------------------------------------

-- slide 13
variable (s : Set ℕ)

example (h0 : ∀ x ∈ s, ¬Even x) (h1 : ∀ x ∈ s, Prime x)
  : ∀x ∈s, ¬Even x ∧ Prime x := by
  intro x xs
  exact ⟨h0 x xs, h1 x xs⟩

example (h : ∃ x ∈ s, ¬Even x ∧ Prime x) : ∃ x ∈ s, Prime x := by
  rcases h with ⟨x, xs, _, prime_x⟩
  exact ⟨x, xs, prime_x⟩

--------------------------------------------------------------

--slide 19
variable {G : Type*} [Group G]

example (a b c : G) : a * b * c = a * (b * c) := by
  exact mul_assoc a b c

example (a : G) : a * a⁻¹ = 1 := by
  exact mul_inv_cancel a

example (a : G) : a⁻¹ * a = 1 := by
  sorry

example (a b : G) (h : a * b = 1) : b * a = 1 := by
  have h' : b =  a⁻¹ := by
    calc b = 1 * b          := by rw [one_mul]
         _ = (a⁻¹ * a) * b  := by rw [← inv_mul_cancel a]
         _ = a⁻¹ * (a * b)  := by rw [mul_assoc]
         _ = a⁻¹ * 1        := by rw [h]
         _ = a⁻¹            := by rw [mul_one]
  rw [h', inv_mul_cancel]


----------------------------------------------------------------

--slide
example : (3 : ℝ ) + 4 = 7 := by
  norm_num

example : (2 : ℝ ) * 3 = 6 := by
  norm_num

example : (3 : ℝ ) * 2 + 1 = 7 := by
  sorry

example : |(-5 : ℝ )| = 5 := by
  norm_num [abs]

example (x y : ℝ) : |x + y| ≤ |x| + |y| := by
  exact abs_add_le x y

example (x : ℝ) : |-x| = |x| := by
  sorry

---------------------------------------------------------------

open Filter Topology
--slide

#check TopologicalSpace ℝ


-- El filtro de entornos de un punto a
#check (𝓝 (0 : ℝ ) : Filter ℝ )

-- Una sucesión tiende a un límite
variable (u : ℕ → ℝ) (L : ℝ)


example : Tendsto (fun n : ℕ => 1 / (n + 1 : ℝ)) atTop (𝓝 0) := by
  refine Metric.tendsto_atTop.mpr ?_
  intro ε hε
  obtain ⟨N, hN⟩: ∃ N : ℕ , (N + 1 : ℝ)⁻¹ < ε := by
    use ⌈(1 / ε)⌉₊
    refine inv_lt_of_inv_lt₀ hε ?_
    rw [one_div]
    have : ε⁻¹ ≤ ↑⌈ε⁻¹⌉₊ := by
      exact Nat.le_ceil ε⁻¹
    linarith
  use N
  intro n hn
  rw [Real.dist_eq]
  simp only [one_div, sub_zero, abs_inv]
  have hrem_abs : |n + (1:ℝ )| = n + 1 := by
    rw [@abs_eq_self]
    linarith
  rw [hrem_abs]
  have hmono: 1/(n + (1:ℝ )) ≤ 1/(N+1) := by
    gcongr
  rw [one_div, one_div] at hmono
  linarith


--------------------------------------------------------------

#min_imports
