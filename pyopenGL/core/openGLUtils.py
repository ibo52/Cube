from  OpenGL import GL

#static methods to load/compile OpenGL shaders
#and link to create GPU porgrams

class OpenGLUtils(object):
    @staticmethod
    def initializeShader(shaderCode, shaderType):
        #specify opengl version and requirements
        extension="#extension GL_ARB_shading_language_420pack: require\n"
        shaderCode="#version 130 \n "+extension+shaderCode

        #create empy shader object and return reference value
        shaderRef=GL.glCreateShader(shaderType)

        #store source code in shader
        GL.glShaderSource(shaderRef,shaderCode)

        #compile source code in shader
        GL.glCompileShader(shaderRef)

        compileSuccess=GL.glGetShaderiv(shaderRef, GL.GL_COMPILE_STATUS)
        if not compileSuccess:
            errorMessage=GL.glGetShaderInfoLog(shaderRef)

            #free the mem reference
            GL.glDeleteShader(shaderRef)

            errorMessage="\n"+errorMessage.decode("utf-8")

            raise Exception(errorMessage)

        #return shaderReference in case of success
        return shaderRef

    @staticmethod
    def initializeProgram(vertexShaderCode,fragmentShaderCode):
        #compile shaders and store references
        vertexShaderRef=OpenGLUtils.initializeShader(vertexShaderCode,GL.GL_VERTEX_SHADER)
        fragmentShaderRef=OpenGLUtils.initializeShader(fragmentShaderCode,GL.GL_FRAGMENT_SHADER)

        #create program reference
        programRef=GL.glCreateProgram()

        GL.glAttachShader(programRef,vertexShaderRef)
        GL.glAttachShader(programRef, fragmentShaderRef)

        #link vertex shader to fragment shader
        GL.glLinkProgram(programRef)

        #check if linking was successfull
        linkSuccess=GL.glGetProgramiv(programRef,GL.GL_LINK_STATUS)
        if not linkSuccess:
            errorMessage=GL.glGetProgramInfoLog(programRef)
            #free the mem references
            GL.glDeleteProgram(programRef)

            errorMessage="\n"+errorMessage.decode("utf-8")

            raise Exception(errorMessage)

        return programRef