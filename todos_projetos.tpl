<!DOCTYPE html>
<html>
	<body>
		<table border="1">
			<th>
				<td>Nome</td>
				<td>Culpado</td>
				<td>Existe esperança?</td>
			</th>
			%for row in rows:
				<tr>
					%for data in row:
						<td>{{data}}</td>
					%end
				</tr>
			%end
		</table>
	</body>
</html>