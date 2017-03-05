<!DOCTYPE html>
<html>
	<body>
		<table border="1">
			<th>
				<td>Nome</td>
				<td>Email</td>
				<td>User</td>
			</th>
			%for row in rows:
				<tr>
					<td></td>
					%for data in row:
						<td>{{data}}</td>
					%end
				</tr>
			%end
		</table>
	</body>
</html>