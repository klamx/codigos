INTERNAL PROCEDURE llenarHijo(dataline ProjectLinesCollection dynamic)
	FOR EACH proceso IN dataline.lines
		susDad is int = HTABLE_Homework.AddChild(sus, proceso.Estado,proceso.Nombre,proceso.NumeroProceso,proceso.fechainicioPlanificacion,proceso.fechafinPlanificacion,proceso.fechaInicioReal,proceso.fechafinreal,proceso.horasReales,proceso.procesoID)
		if proceso.procesoID = newProjectsCreateOperationLinesController.localProjectLines.procesoPadreID THEN
			proceso.lines.addTrabajo(newProjectsCreateOperationLinesController.localProjectLines)
			
		else
			llenarHijo(proceso.lines)	
		END
	END
END
	
IF newProjectsCreateOperationLinesController.localProjectLines.procesoPadreID = "" THEN
	localProjects.lines.addTrabajo(newProjectsCreateOperationLinesController.localProjectLines)
ELSE
	for each proceso in localProjects.lines.lines
		llenarHijo(proceso.lines)
	END
END

