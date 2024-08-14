def read_obj(file_path):
    vertices = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('v '):
                vertex = [float(coord) for coord in line.strip().split()[1:]]
                vertices.append(vertex)
    return vertices

def convert_to_particle_commands(vertices, particle_type, scale=1):
    commands = []
    for vertex in vertices:
        x, y, z = vertex
        x *= scale
        y *= scale
        z *= scale
        command = f'/particle {particle_type} {x} {y} {z} 1 1 1 0 1 force'
        commands.append(command)
    return commands

def write_to_mcfunction(commands, output_file):
    with open(output_file, 'w') as file:
        for command in commands:
            file.write(command + '\n')

# 示例用法
obj_file_path = 'model.obj'
particle_type = 'minecraft:flame'
scale = 0.1  # 调整比例
mcfunction_file = 'particles.mcfunction'

vertices = read_obj(obj_file_path)
particle_commands = convert_to_particle_commands(vertices, particle_type, scale)
write_to_mcfunction(particle_commands, mcfunction_file)