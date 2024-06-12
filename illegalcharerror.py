def t_error(t):
  print(f"IllegalCharError: illegal character or token at '{t.value}', position {t.lexpos}, line {t.lineno}.")
  t.lexer.skip(1)
